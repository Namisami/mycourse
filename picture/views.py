from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from album.models import Album
from category.models import Category
from picture.models import Picture
from picture.forms import PictureMainEditForm, PictureSubcategoryEditForm
from subcategory.models import Subcategory
from authentication.models import User


@login_required
def picture(request, picture_id):
    user = User.objects.get(id=request.user.id)
    picture = get_object_or_404(Picture, id=picture_id, owner=user)
    album = get_object_or_404(Album, picture=picture.id, owner=user)
    context = {
        'picture': picture,
        'album': album,
        }
    return render(request, 'picture/picture.html', context)

@login_required
def edit(request, picture_id):
    user = User.objects.get(id=request.user.id)
    picture = get_object_or_404(Picture, id=picture_id, owner=user)
    album = get_object_or_404(Album, picture=picture.id, owner=user)
    category = picture.category

    if request.method == 'POST':
        form = PictureMainEditForm(request.POST, instance=picture)
        if form.is_valid():
            if Category.objects.get(id=request.POST.get("category")) != category:
                for subcategory in picture.subcategory.all():
                    picture.subcategory.remove(subcategory.id)
            form.save()
            return HttpResponseRedirect(reverse('picture', kwargs={'picture_id': picture.id}))
    else:
        form = PictureMainEditForm(instance=picture)
    context = {
        'form': form,
        'picture': picture,
        'album': album,
        }
    return render(request, 'picture/picture.html', context)

@login_required
def edit_subcategory(request, picture_id):
    user = User.objects.get(id=request.user.id)
    picture = get_object_or_404(Picture, id=picture_id, owner=user)
    album = get_object_or_404(Album, picture=picture.id, owner=user)

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
        form = PictureSubcategoryEditForm(instance=picture)
        form.fields["subcategory"].queryset = Subcategory.objects.filter(category=picture.category.id)
    context = {
        'form': form,
        'picture': picture,
        'album': album,
        }
    return render(request, 'picture/picture.html', context)
    
@login_required
def delete(request, picture_id):
    user = User.objects.get(id=request.user.id)
    picture = get_object_or_404(Picture, id=picture_id, owner=user)
    album = get_object_or_404(Album, picture=picture.id, owner=user)
    picture.delete()
    return HttpResponseRedirect(reverse('album', kwargs={'album_id': album.id}))