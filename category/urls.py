from category import views
from django.urls import path, include


urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>', views.category, name='category'),
    path('create/', views.create, name='category_create'),
    path('<int:category_id>/subcategory/', include('subcategory.urls')),
]