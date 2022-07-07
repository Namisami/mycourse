from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from album.models import Album
from album.forms import PictureForm, AlbumEditForm
from django.contrib.auth.decorators import login_required
from authentication.models import User


@login_required
def index(request):
    user = User.objects.get(id=request.user.id)
    albums = Album.objects.filter(owner=user)
    title = "title"
    created_at = "created_at"
    try:
        order = request.GET["orderby"]
        if order == "title":
            title = ""
        else:
            title = "title"
        if order == "created_at":
            created_at = ""
        else:
            created_at = "created_at"
        albums = albums.order_by(order)
    except:
        pass
    if not(albums):
        Album.objects.create(owner=user)
        albums = Album.objects.filter(owner=user)
    context = {
        'albums': albums,
        'title': title,
        'created_at': created_at,
    }
    return render(request, 'album/index.html', context)

@login_required
def album(request, album_id):
    user = User.objects.get(id=request.user.id)
    album = get_object_or_404(Album, id=album_id, owner=user)
    pictures = album.picture.all()

    upload_date = "-upload_date"
    try:
        order = request.GET["orderby"]
        if order == "-upload_date":
            upload_date = ""
        else:
            upload_date = "-upload_date"
        pictures = pictures.order_by(order)
    except:
        pass

    # Добавление фото
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.owner = user
            picture.save()
            album.picture.add(picture)
            
            context = {
                'form': form,
                'album': album,
                'pictures': pictures,
                "upload_date": upload_date,
            }
            return render(request, 'album/album.html', context)
    else:
        form = PictureForm()
    context = {
        'form': form,
        'album': album,
        'pictures': pictures,
        "upload_date": upload_date,
        }

    return render(request, 'album/album.html', context)

@login_required
def edit(request, album_id):
    user = User.objects.get(id=request.user.id)
    album = get_object_or_404(Album, id=album_id, owner=user)
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            about = form.save(commit=False)
            about.owner = user
            about.save()
            context = {
                'album': album,
            }
            return HttpResponseRedirect(reverse('album', kwargs={'album_id': album.id}))
    else:
        form = AlbumEditForm(instance=album)
    context = {
        'form': form,
        'album': album,
        }
    return render(request, 'album/edit.html', context)

@login_required
def create(request):
    user = User.objects.get(id=request.user.id)
    album = Album.objects.create(owner=user)
    return HttpResponseRedirect(reverse('album', kwargs={'album_id': album.id}))

@login_required
def delete(request, album_id):
    user = User.objects.get(id=request.user.id)
    album = get_object_or_404(Album, id=album_id, owner=user)
    album.delete()
    return HttpResponseRedirect(reverse('index'))