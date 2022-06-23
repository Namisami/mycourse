from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from album.models import Album
from album.forms import AlbumForm, PictureForm

def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'album/index.html', context)

def album(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save()
            album.picture.add(picture)
            context = {
                'form': form,
                'album': album,
            }
            return render(request, 'album/album.html', context)
    else:
        form = PictureForm()
    context = {
        'form': form,
        'album': album,
        }

    return render(request, 'album/album.html', context)

def create(request, latest_album_id):
    latest_album_id = int(latest_album_id) + 1
    Album.objects.get_or_create(id=latest_album_id)
    return HttpResponseRedirect(reverse('album', kwargs={'album_id': latest_album_id}))