# Generated by Django 4.2.2 on 2023-06-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0009_remove_my_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='nickname',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
