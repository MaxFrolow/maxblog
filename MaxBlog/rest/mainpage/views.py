

from rest_framework  import generics
from rest.mainpage.serializers import PostDetailSerializer, PostListSerializer
from mainpage.models import Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest.mainpage.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets


class PostAPICreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer

class PostAPIListView(generics.ListAPIView, viewsets.ModelViewSet):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser, )


class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly, )
