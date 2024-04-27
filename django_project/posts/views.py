from django.shortcuts import render
from rest_framework import generics 
from .models import Post
from .serializer import PostSerializer
# Create your views here.

class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    