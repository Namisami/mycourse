# Generated by Django 4.0.5 on 2022-06-23 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
        ('picture', '0006_alter_picture_author_alter_picture_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory', verbose_name='Подкатегория'),
        ),
    ]
