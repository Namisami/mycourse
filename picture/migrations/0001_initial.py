# Generated by Django 4.0.5 on 2022-06-30 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('category', '0001_initial'),
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_file', models.ImageField(blank=True, upload_to='pictures', verbose_name='Изображение')),
                ('upload_date', models.DateField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.author', verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
                ('subcategory', models.ManyToManyField(blank=True, to='subcategory.subcategory', verbose_name='Подкатегории')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
