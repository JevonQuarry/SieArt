from django.db import models
from django.db import models
from apps.posts.models import Post
from apps.users.models import User

from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.

class Comment(models.Model):
    class Meta(object):
        db_table = 'comment'

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, db_index=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=False, null=True, db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    comment = models.CharField(
        'Comment', blank=False, null=True, db_index=True, max_length=500

    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )