# Generated by Django 3.0.6 on 2020-05-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
