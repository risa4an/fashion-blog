from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    article_name = models.CharField( max_length= 100)
    article_text = models.TextField()
    article_image = models.TextField()
    article_date = models.DateTimeField()
    article_author = models.CharField( max_length = 50)

    def latest_articles(self):
        list_of_articles = Article.objects.order_by('-время публикации')[:10]
        return list(list_of_articles)

    @property
    def image_url(self):
        if self.article_image and hasattr(self.article_image, 'url'):
            return self.article_image.url


class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete= models.CASCADE)
    comment_author  = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.CharField( max_length= 200)
    comment_data = models.DateTimeField()