from unicodedata import name
from album import views
from django.urls import path

APP_NAME = "album"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.album, name='album'),
    path('<int:latest_album_id>/create/', views.create, name='create'),
    # path('<int:album_id>/upload/', views.image_upload_view)
    # path('<int:album_id>/add/', views.add, name='add'),
]
