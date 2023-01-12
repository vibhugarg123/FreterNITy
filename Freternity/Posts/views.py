from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render,get_object_or_404 , redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import authenticate

from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q
#from comments.models import Comment
#from comments.forms import CommentForm

def home_page(request):
    return HttpResponse("Hello world")

def post_create(request):
    #if not request.user.is_staff or not request.user.is_superuser:
    #   raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)