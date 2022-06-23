from album import views
from django.urls import path, include

APP_NAME = "album"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.album, name='album'),
    path('<int:latest_album_id>/create/', views.create, name='create'),
]
