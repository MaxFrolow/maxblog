

from rest_framework  import generics
from rest.mainpage.serializers import PostDetailSerializer, PostListSerializer
from mainpage.models import Post


class PostAPICreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer

class PostAPIListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()