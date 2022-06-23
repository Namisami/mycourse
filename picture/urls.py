from picture import views
from django.urls import path

APP_NAME = "picture"

urlpatterns = [
    # path('', views.index, name='index'),
    path('<int:picture_id>/', views.picture, name='picture'),
    path('<int:picture_id>/edit/', views.edit, name='edit'),
    path('<int:picture_id>/edit_subcategory/', views.edit_subcategory, name='edit_subcategory'),
]
