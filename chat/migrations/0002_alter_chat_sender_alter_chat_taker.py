# Generated by Django 4.2.2 on 2023-07-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0012_delete_chat'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_chats', to='myusers.my_user'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_chats', to='myusers.my_user'),
        ),
    ]
