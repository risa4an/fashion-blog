from django.contrib import admin
from .models import Photo, Photographer
# Register your models here.
admin.site.register(Photographer)
admin.site.register(Photo)