from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'photographers'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:album_id>/', views.detail, name = 'detail'),
    path('addalbum/',  views.add_album, name='add_album'),
    path('<int:album_id>/editalbum/', views.edit_album, name = 'edit_album'),
    path('<int:album_id>/delete/<int:photo_id>/', views.delete_photo, name = 'delete_photo'),
    path('<int:album_id>/add_photo/', views.add_photo, name = 'add_photo'),
    path('<int:album_id>/delete_album/', views.delete_album, name = 'delete_album')

]

# if settings.DEBUG:
#     if settings.MEDIA_ROOT:
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# urlpatterns += staticfiles_urlpatterns()