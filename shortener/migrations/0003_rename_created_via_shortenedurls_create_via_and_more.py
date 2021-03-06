# Generated by Django 4.0.4 on 2022-05-02 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_users_url_count_alter_shortenedurls_prefix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortenedurls',
            old_name='created_via',
            new_name='create_via',
        ),
        migrations.RenameField(
            model_name='shortenedurls',
            old_name='created_by',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='shortenedurls',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='shortenedurls',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shortener.categories'),
        ),
        migrations.AddIndex(
            model_name='shortenedurls',
            index=models.Index(fields=['prefix', 'shortened_url'], name='shortener_s_prefix_bbcd1e_idx'),
        ),
    ]
