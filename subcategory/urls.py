from subcategory import views
from django.urls import path, include


urlpatterns = [
    path('<int:subcategory_id>/', views.subcategory, name='subcategory'),
    path('create/', views.create, name='subcategory_create'),
    path('<int:subcategory_id>/edit/', views.edit, name='subcategory_edit'),
    path('<int:subcategory_id>/delete/', views.delete, name='subcategory_delete'),
]