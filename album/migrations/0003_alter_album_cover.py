# Generated by Django 4.0.5 on 2022-06-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='albums/covers', verbose_name='Обложка'),
        ),
    ]
