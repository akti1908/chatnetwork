# Generated by Django 4.2.2 on 2023-06-28 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0008_alter_my_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_user',
            name='nickname',
        ),
    ]
