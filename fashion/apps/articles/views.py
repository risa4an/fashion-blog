from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import datetime
from .models import Article,Comment
from django.urls import reverse
from django.contrib import auth

def index(request):
    latest_article_list = Article.objects.all().order_by('-id')[:5]
    return render(request, 'articles/list_of_articles.html',{'latest_article_list':latest_article_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Такую статью еще не написали)")
    latest_comments = a.comment_set.all().order_by('-id')[:10]
    return render(request,'articles/detail.html', {'article' : a, 'latest_comments' : latest_comments})

@csrf_protect
@login_required
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Такую статью еще не написали)")

    if request.user.is_authenticated:
        comment = Comment()
        comment.comment_article = a
        comment.comment_author = auth.get_user(request)
        comment.comment_text = request.POST['text']
        comment.comment_data = datetime.datetime.now()
        comment.save()


    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)) )
