from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentList.as_view(), name='comment_list'),
    path('', views.CommentUpdate.as_view(), name='comment_Update'),
    path('add/', views.CommentAdd.as_view(), name='comment_add'),
    path('delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
]