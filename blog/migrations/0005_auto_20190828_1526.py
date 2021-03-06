# Generated by Django 2.2.4 on 2019-08-28 15:26

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190828_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(storage=blog.models.authorDirectory, upload_to='', verbose_name='آواتار'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(storage=blog.models.categoryDirectory, upload_to='', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='story',
            name='CoverImage',
            field=models.ImageField(storage=blog.models.storyDirectory, upload_to='', verbose_name='عکس کاور'),
        ),
        migrations.AlterField(
            model_name='story',
            name='thumbNailImage',
            field=models.ImageField(storage=blog.models.storyDirectory, upload_to='', verbose_name='عکس کوچک'),
        ),
    ]
