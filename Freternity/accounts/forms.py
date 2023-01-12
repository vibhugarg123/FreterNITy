from __future__ import unicode_literals
from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

User=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User Doesn't Exist or Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError("User Is Not Active")
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):

    email2=forms.EmailField(label='Confirm Email')
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'email2',
            'password'
        ]
    def clean_email2(self):
        email=self.cleaned_data.get('email')
        email2=self.cleaned_data.get('email2')
        if email!=email2:
            raise forms.ValidationError("Emails Doesn't Match")
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already Exists")
        return email
