# Generated by Django 3.0.6 on 2020-06-14 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20200614_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='mial',
            new_name='mail',
        ),
    ]
