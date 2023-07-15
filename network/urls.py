from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.homeFeeds, name='homeFeeds'),
    path('signUp', views.signUp, name='register'),
    path('signIn', views.signIn, name='login'),
    path('signOut', views.signOut, name='logout'),
]
