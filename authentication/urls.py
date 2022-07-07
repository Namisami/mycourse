from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views, name = "login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html')),
]