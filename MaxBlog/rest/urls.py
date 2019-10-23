
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter


from rest.mainpage import views as mainpageViews
from rest.accounts import views as accountsViews

app_name = 'rest'

router = DefaultRouter()
router.register('account/users', accountsViews.UserViewSet)
router.register('post/all', mainpageViews.PostAPIListView)





urlpatterns = [
    #rest for post
    path('v1/post/create', mainpageViews.PostAPICreateView.as_view()),
    path('v1/post/detail/<int:pk>/', mainpageViews.PostAPIDetailView.as_view()),

    #rest authorisation
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),


    ]