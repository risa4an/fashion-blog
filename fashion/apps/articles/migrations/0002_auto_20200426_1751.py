# Generated by Django 3.0.5 on 2020-04-26 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='автор статьи',
            new_name='article_author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='время публикации',
            new_name='article_date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='изображения для статьи',
            new_name='article_image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='название статьи',
            new_name='article_name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='текст статьи',
            new_name='article_text',
        ),
    ]