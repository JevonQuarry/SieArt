from django.shortcuts import render
from rest_framework import generics
from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.order_by('-created_at').all()
    serializer_class = PostSerializer


class PostAdd(generics.CreateAPIView, CustomLoginRequiredMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    


class PostUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer