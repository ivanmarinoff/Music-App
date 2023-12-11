from django.shortcuts import render, redirect
from rest_framework import viewsets
from MusicApp.music_app.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MusicApp.music_app.models import Profile, Album
from MusicApp.music_app.serializers import ProfileSerializer, AlbumSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer



def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def index(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return profile_add(request)
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'common/home-with-profile.html', context)


def add_album(request):
    profile = get_profile()
    form = AlbumCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()
    context = {
        'profile': profile,
        'album': album,
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()
    form = AlbumEditForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()
    form = AlbumDeleteForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }
    return render(request, 'album/delete-album.html', context)


def profile_add(request):
    profile = get_profile()
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'common/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    album_count = Album.objects.all().count()
    context = {
        'profile': profile,
        'album_count': album_count
    }
    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    album = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        album.delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
