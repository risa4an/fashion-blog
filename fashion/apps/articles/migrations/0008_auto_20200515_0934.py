# Generated by Django 3.0.5 on 2020-05-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200515_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
