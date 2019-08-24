from .models import Post
import django_filters


class UserPostMixin:
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

