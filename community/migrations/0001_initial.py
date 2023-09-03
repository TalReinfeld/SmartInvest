# Generated by Django 4.2.4 on 2023-08-30 09:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stockAnalysis', '0001_initial'),
        ('users', '0002_test_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='NO DESCRIPTION')),
                ('title', models.CharField(default=models.BigAutoField(primary_key=True, serialize=False),
                                           max_length=50)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('analysis_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                     to='stockAnalysis.analyzedstock')),
                ('likes', models.ManyToManyField(blank=True, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_comments', to='users.profile')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.post')),
                ('publisher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='published_comments', to='users.profile')),
            ],
        ),
    ]
