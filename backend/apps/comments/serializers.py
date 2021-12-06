from .models import Post
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(allow_null=True)

    class Meta:
        model = Post
        fields = '__all__'