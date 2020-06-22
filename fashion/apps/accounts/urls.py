from django.contrib.auth import views
from django.urls import path

from fashion.apps.accounts.views import signup_view, activation_sent_view, activate

app_name = 'accounts'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', signup_view, name='register'),
    path('register/sent/', activation_sent_view, name='activation_sent_view'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]