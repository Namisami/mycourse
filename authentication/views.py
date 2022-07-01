from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from authentication.forms import CustomUserCreationForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")
    template_name = "authentication/signup.html"