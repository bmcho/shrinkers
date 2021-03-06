# Generated by Django 4.0.4 on 2022-05-02 07:32

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='url_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shortenedurls',
            name='prefix',
            field=models.CharField(default=shortener.models.ShortenedUrls.rand_letter, max_length=50),
        ),
    ]
