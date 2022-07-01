from subcategory import views
from django.urls import path, include


urlpatterns = [
    path('<int:subcategory_id>', views.subcategory, name='subcategory'),
    path('create/', views.create, name='subcategory_create'),
]