from picture import views
from django.urls import path

APP_NAME = "picture"

urlpatterns = [
    path('<int:picture_id>/', views.picture, name='picture'),
    path('<int:picture_id>/delete/', views.delete, name='picture_delete'),
    path('<int:picture_id>/edit/', views.edit, name='edit'),
    path('<int:picture_id>/edit_subcategory/', views.edit_subcategory, name='edit_subcategory'),
]
