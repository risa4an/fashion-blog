from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Photographer, Photo
from .forms import PostForm, PhotoForm
# Create your views here.

def index(request):
    photographers_list = Photographer.objects.all().order_by('-id')[:5]
    return (render(request, 'photographers/photographer_list.html', {'photographers_list' : photographers_list}))

def detail (request, album_id):
    album = Photographer.objects.get(id = album_id)
    photo_list = album.photo_set.all()
    return (render(request,'photographers/detail.html', {'album' : album, 'photo_list' : photo_list} ))

def add_album(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.photographer = request.user
            post.published_date = datetime.now()
            post.save()
            return HttpResponseRedirect(reverse('photographers:index' ))
    else:
        form = PostForm()
    return render(request, 'photographers/add_album.html', {'form': form})

def edit_album(request, album_id):
    post = get_object_or_404(Photographer, id = album_id)
    form = PostForm(request.POST, instance=post)
    if (request.method == "POST"):
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.photographer = request.user
            post.published_date = datetime.now()
            post.save()
            photographers_list = Photographer.objects.all().order_by('-id')[:5]
            return (render(request, 'photographers/photographer_list.html', {'photographers_list' : photographers_list}))
        else:
            form = PostForm(instance = post)
    return render(request, 'photographers/edit_album.html', {'form' : form, 'album' : post})

def delete_photo(request, album_id, photo_id):
    photo = Photo.objects.get(id = photo_id)
    if (photo.photo_album.photographer == request.user):
        photo.delete()
    return HttpResponseRedirect(reverse('photographers:detail', args = (album_id, )))

def delete_album(request, album_id):
    album = Photographer.objects.get(id = album_id)
    if (request.user == album.photographer):
        album.delete()
    return HttpResponseRedirect(reverse('photographers:index'))

def add_photo(request, album_id):
    album = Photographer.objects.get(id = album_id)
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.photo_album = album
            post.save()
            return HttpResponseRedirect(reverse('photographers:detail', args = (album_id, ) ))
    else:
        form = PhotoForm()
    return render(request, 'photographers/add_photos.html', {'form': form, 'album': album})