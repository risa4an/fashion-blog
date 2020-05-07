from django.contrib.auth import views
from django.urls import path

from fashion.apps.accounts.views import RegisterFormView
app_name = 'accounts'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='regiser'),

]