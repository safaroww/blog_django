from django.contrib import admin
from django.urls import path
from post import views


urlpatterns = [
    path('post/<int:pk>/<str:slug>', views.post, name='post'),
]