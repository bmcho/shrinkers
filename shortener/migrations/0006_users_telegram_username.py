# Generated by Django 4.0.4 on 2022-05-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_statistic_custom_params_trackingparams'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='telegram_username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
