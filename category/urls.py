from category import views
from django.urls import path, include


urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>', views.category, name='category'),
]