# Generated by Django 3.0.6 on 2020-06-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '文章列表'},
        ),
        migrations.AlterField(
            model_name='article',
            name='auth',
            field=models.CharField(max_length=20, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后更新时间'),
        ),
    ]