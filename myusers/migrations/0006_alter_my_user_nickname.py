# Generated by Django 4.2.2 on 2023-06-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0005_alter_my_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='nickname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]