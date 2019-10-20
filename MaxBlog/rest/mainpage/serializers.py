from rest_framework import serializers
from mainpage.models import Post, Comment

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created_datetime', 'title', 'author')