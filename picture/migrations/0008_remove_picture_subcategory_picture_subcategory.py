# Generated by Django 4.0.5 on 2022-06-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
        ('picture', '0007_picture_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='picture',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='subcategory.subcategory', verbose_name='Подкатегории'),
        ),
    ]