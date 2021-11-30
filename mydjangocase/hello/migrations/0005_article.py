# Generated by Django 3.0.6 on 2020-06-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20200527_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('auth', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
