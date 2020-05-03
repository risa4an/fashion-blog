from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    latest_article_list = Article.objects.all()[:5]
    return render(request, 'articles/list_of_articles.html',{'latest_article_list':latest_article_list})