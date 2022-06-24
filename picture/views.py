from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from album.models import Album
from picture.models import Picture
from picture.forms import PictureMainEditForm, PictureSubcategoryEditForm
from subcategory.models import Subcategory
from subcategory.forms import SubcategoryForm

def picture(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    album = Album.objects.get(picture=picture.id)
    context = {
        'picture': picture,
        'album': album,
        }
    return render(request, 'picture/picture.html', context)

def edit(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    album = Album.objects.get(picture=picture.id)

    if request.method == 'POST':
        form = PictureMainEditForm(request.POST, instance=picture)
        if form.is_valid():
            if request.POST.get("category") != picture.category:
                for subcategory in picture.subcategory.all():
                    picture.subcategory.remove(subcategory.id)
            form.save()
            return HttpResponseRedirect(reverse('picture', kwargs={'picture_id': picture.id}))
    else:
        form = PictureMainEditForm()
    context = {
        'form': form,
        'picture': picture,
        'album': album,
        }
    return render(request, 'picture/picture.html', context)

def edit_subcategory(request, picture_id):
    picture = Picture.objects.get(id=picture_id)

    if request.method == 'POST':
        form = PictureSubcategoryEditForm(request.POST, instance=picture)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'picture': picture,
            }
            return HttpResponseRedirect(reverse('picture', kwargs={'picture_id': picture.id}))
    else:
        form = PictureSubcategoryEditForm()
        form.fields["subcategory"].queryset = Subcategory.objects.filter(category=picture.category.id)
    context = {
        'form': form,
        'picture': picture,
        }
    return render(request, 'picture/picture.html', context)