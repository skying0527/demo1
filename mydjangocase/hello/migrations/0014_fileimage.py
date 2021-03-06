# Generated by Django 3.0.6 on 2020-06-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0013_auto_20200616_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('image', models.ImageField(blank=True, upload_to='up_image', verbose_name='上传图片')),
                ('fiels', models.FileField(blank=True, upload_to='up_file', verbose_name='上传文件')),
                ('add_time', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '上传图片',
                'verbose_name_plural': '上传图片',
            },
        ),
    ]
