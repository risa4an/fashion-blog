from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from django.utils import timezone

from .models import Photographer, Photo
@pytest.mark.django_db
def test_str():
    usr = User.objects.create_user('katya', 'simplepassword')
    album = Photographer(photographer=usr, name='new album', discription='great new story')
    photo = Photo(photo_album=album, photo_image='dfgdfg', photo_name='the begining')
    assert str(album) == 'new album'
    assert str(photo) == 'the begining'

@pytest.mark.django_db
def test_index(client):
    url = reverse('photographers:index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_viewalbum(client):
    usr = User.objects.create_user(username='katya1', password='simplepassword', email='katya.risunova@gmail.com')
    usr.save()
    usr.is_active = True
    usr.save()
    usr = User.objects.create_user(username='katya', password='simplepassword', email='katya.risunova@gmail.com')
    usr.save()
    usr.is_active = True
    usr.save()
    client.login(username='katya', password='simplepassword')
    url = reverse('photographers:add_album')
    response = client.post(url, {'name' : 'new album', 'discription':'great news story'})
    assert response.status_code == 302
    assert Photographer.objects.count() == 1
    url = reverse('photographers:detail', args=[1])
    response = client.get(url)
    assert response.status_code == 200
    url = reverse('photographers:add_photo', args=[1])
    response = client.post(url, {'photo_name' : 'new photo', 'photo_image' : 'swefws'})
    assert response.status_code == 302
    url = reverse('photographers:edit_album', args=[1])
    response = client.post(url, {'name' : 'new album', 'discription':'great news story'})
    assert response.status_code == 200
    url = reverse('photographers:delete_photo', args=[1, 1])
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('photographers:delete_album', args = [1])
    response = client.get(url)
    assert response.status_code == 302
    album = Photographer.objects.create(photographer=usr, name='new album', discription='great story')
    photo = Photo.objects.create(photo_name='new photo', photo_image='dfgrg', photo_album=album)

    client.login(username='katya1', password='simplepassword')
    url = reverse('photographers:edit_album', args=[1])
    response = client.post(url, {'name': 'new album', 'discription': 'great news story'})
    assert response.status_code == 404
    url = reverse('photographers:delete_photo', args=[album.id, photo.id])
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('photographers:delete_album', args=[album.id])
    response = client.get(url)
    assert response.status_code == 302

