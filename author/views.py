from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from author.models import Author
from author.forms import AuthorForm


@login_required
def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'author/authors.html', context)

@login_required
def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {
        'author': author,
    }
    return render(request, 'author/author.html', context)

# @login_required
# def edit(request, author_id):
#     author = get_object_or_404(Author, id=author_id)
#     if request.method == 'POST':
#         form = AuthorForm(request.POST, instance=author)
#         if form.is_valid():
#             form.save()
#             context = {
#                 'form': form,
#             }
#             return HttpResponseRedirect(reverse('author', kwargs={'author': author}))
#     else:
#         form = AuthorForm(instance=author)
#     context = {
#         'form': form,
#         }
#     return render(request, 'author/edit.html', context)

# @login_required
# def delete(request, author_id):
#     author = get_object_or_404(Author, id=author_id)
#     author.delete()
#     context = {
#         'author': author,
#     }
#     return HttpResponseRedirect(reverse('authors'))

@login_required
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