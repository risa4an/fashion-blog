from django.contrib import admin
from .models import Article, Comment
# Register your models here.

# admin.site.register(Article)
# admin.site.register(Comment)
class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'article_author')
    inlines = [CommentInline]
admin.site.register(Article, ArticleAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'comment_article')

