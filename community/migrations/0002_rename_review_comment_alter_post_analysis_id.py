# Generated by Django 4.2 on 2023-06-28 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockAnalysis', '0001_initial'),
        ('users', '0001_initial'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='analysis_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stockAnalysis.analyzedstocks'),
        ),
    ]