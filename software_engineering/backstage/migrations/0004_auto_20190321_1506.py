# Generated by Django 2.1.7 on 2019-03-21 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0003_auto_20190321_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='code',
            new_name='codename',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nickname',
        ),
    ]