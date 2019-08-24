"""MaxBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


app_name = 'mainpage'
urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name="detail"),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/post/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path(r'comment_create/<int:post_id>', views.CommentCreateView.as_view(), name='comment_create'),
    path('my_posts', views.MyPostsView.as_view(), name="my_posts"),
    ]




