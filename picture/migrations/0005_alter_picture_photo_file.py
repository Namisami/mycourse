# Generated by Django 4.0.5 on 2022-06-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_alter_picture_author_alter_picture_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo_file',
            field=models.ImageField(blank=True, upload_to='pictures', verbose_name='Изображение'),
        ),
    ]
