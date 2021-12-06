from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment

# Create your views here.

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.order_by('-created_at').all()
    serializer_class = CommentSerializer


class CommentAdd(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer