from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from django.utils import timezone

from .models import Article, Comment
from fashion.apps.accounts.tests import auto_login_user
import datetime

@pytest.mark.django_db
def test_create_articles():
    for i in range(10):
        artcl = Article(article_name='Great story' + str(i), article_text='new breathtaking adventure', article_author='Karolina', article_date=timezone.now())
        artcl.save()
    assert Article.objects.count() == 10
    assert str(artcl) == 'Great story9'

@pytest.mark.django_db
def test_create_comment(client):
    artcl = Article(article_name='Great story', article_text='new breathtaking adventure', article_author='Karolina', article_date=timezone.now())
    artcl.save()
    usr = User.objects.create_user('katya', 'simplepassword')
    com = Comment(comment_author=usr, comment_text='mmmm cool', comment_data=timezone.now(), comment_article=artcl)
    com.save()
    assert Comment.objects.count() == 1
    assert str(com) == 'mmmm cool'

@pytest.mark.django_db
def test_auth_view(client):
    url = reverse('articles:index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_article_view(client):
    artcl = Article(article_name='Great story', article_text='new breathtaking adventure', article_author='Karolina',
                    article_date=timezone.now())
    artcl.save()
    usr = User.objects.create_user(username='katya', password='simplepassword', email='katya.risunova@gmail.com')
    usr.save()
    usr.is_active = True
    usr.save()
    client.login(username='katya', password='simplepassword')
    url = reverse('articles:detail', args=[artcl.id])
    responce = client.post(url, {'comment_text' : "great article!)"})
    assert responce.status_code == 302
    assert artcl.comment_set.count() == 1
    url = reverse('articles:detail', args=[10])
    responce = client.get(url)
    assert responce.status_code == 404








