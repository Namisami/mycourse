from album import views
from django.urls import path, include

APP_NAME = "album"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.album, name='album'),
    path('<int:album_id>/edit/', views.edit, name='album_edit'),
    path('<int:album_id>/delete/', views.delete, name='album_delete'),
    path('create/', views.create, name='create'),
]
