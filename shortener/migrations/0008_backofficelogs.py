# Generated by Django 4.0.4 on 2022-05-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0007_schedules'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackOfficeLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('endpoint', models.CharField(blank=True, max_length=2000, null=True)),
                ('body', models.JSONField(null=True)),
                ('method', models.CharField(blank=True, max_length=20, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=30, null=True)),
                ('status_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
