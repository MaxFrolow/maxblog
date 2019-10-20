
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'rest'
from rest.mainpage import views as mainpageViews

urlpatterns = [
    path('post/create', mainpageViews.PostAPICreateView.as_view()),
    path('post/all', mainpageViews.PostAPIListView.as_view()),
    path('post/detail/<int:pk>/', mainpageViews.PostAPIDetailView.as_view()),
    ]