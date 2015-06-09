from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request,'blog/post_list.html',{'posts':posts})