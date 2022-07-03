from django.contrib import admin
from django.urls import path, include
from author import views


urlpatterns = [
    path('', views.authors, name='authors'),
    path('<int:author_id>', views.author, name='author'),
    path('add/', views.add, name='author_add'),
]