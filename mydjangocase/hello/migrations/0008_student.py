# Generated by Django 3.0.6 on 2020-06-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_bank_card_carddetail_cardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30, verbose_name='学号')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('score', models.IntegerField(verbose_name='分数')),
            ],
            options={
                'verbose_name': '学生成绩',
                'verbose_name_plural': '学生成绩',
            },
        ),
    ]
