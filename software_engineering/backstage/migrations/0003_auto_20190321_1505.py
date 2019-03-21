# Generated by Django 2.1.7 on 2019-03-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0002_user_end_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(default='2016', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]