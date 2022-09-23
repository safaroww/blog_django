from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:pk>', views.author, name='author'),
]

