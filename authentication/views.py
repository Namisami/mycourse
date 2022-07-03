from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from authentication.forms import CustomUserCreationForm, CustomUserChangeForm
from authentication.models import User

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")
    template_name = "authentication/signup.html"

@login_required
def profile(request):
    return render(request, 'authentication/profile.html')

def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
            }
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        }
    return render(request, 'authentication/edit.html', context)