# Generated by Django 4.2.2 on 2023-07-01 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0012_delete_chat'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='like',
            name='unique_like',
        ),
        migrations.AlterField(
            model_name='like',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myusers.my_user'),
        ),
    ]