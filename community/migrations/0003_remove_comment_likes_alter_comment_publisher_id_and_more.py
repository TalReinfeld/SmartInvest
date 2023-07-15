# Generated by Django 4.2.2 on 2023-07-14 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_test_data'),
        ('community', '0002_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='publisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_comments', to='users.profile'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to='users.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, to='users.profile'),
        ),
    ]
