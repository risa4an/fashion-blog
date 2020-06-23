

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashion.settings")
import uuid
import pytest
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .tokens import account_activation_token


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('katya', 'katya.risunova@gmail.com', 'justmypassword')

    assert User.objects.count() == 1

@pytest.mark.django_db
def test_signup_view(client):
    url = reverse('accounts:register')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signin_view(client):
    url = reverse('accounts:login')
    response = client.get(url)
    assert response.status_code == 200

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        kwargs['password'] = 'test_password'
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user

@pytest.fixture
def auto_login_user(db, client, create_user):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password='test_password')
        return client, user

    return make_auto_login

@pytest.mark.django_db
def test_auth_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('accounts:register')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_activate_view(auto_login_user):
    client, user = auto_login_user()
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    url = reverse('accounts:activate', args=[uid, token])
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_form_signup(client):
    data = {'username' : 'Ekatekage', 'email':'katya.risunova@gmail.com', 'password1':'helloitsme',  'password2':'helloitsme'}
    url = reverse('accounts:register')

    response = client.post(url, data)
    usr = User.objects.get(username='Ekatekage')

    uid = urlsafe_base64_encode(force_bytes(usr.pk))
    token = account_activation_token.make_token(usr)
    url2 = reverse('accounts:activate', args=[uid, token])
    response2 = client.get(url2)
    assert response.status_code == 302
    assert response2.status_code == 302






