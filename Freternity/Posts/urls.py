from django.conf.urls import url
from . import views

urlpatterns = [
    #/posts/
    url(r'^create/$',views.post_create,name='create'),
]