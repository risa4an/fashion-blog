from django.contrib import admin
from .models import Photo, Photographer
# Register your models here.
# admin.site.register(Photographer)
# admin.site.register(Photo)

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('name', 'photographer')
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_name', 'photo_album')
