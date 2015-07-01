from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Album
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view()
def album_list(request):
    albums = Album.objects.using('music').all()
    return Response(albums)