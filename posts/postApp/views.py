from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import Post
from rest_framework import viewsets
from .serialisers import Postserialisers

# Create your views here.
class PostViws(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = Postserialisers