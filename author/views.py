from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from author.models import Author
from author.forms import AuthorForm


def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'author/authors.html', context)

def add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
            }
            return HttpResponseRedirect(reverse('authors'))
    else:
        form = AuthorForm()
    context = {
        'form': form,
        }
    return render(request, 'author/add.html', context)