# Generated by Django 4.2.1 on 2023-06-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatroom_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='message',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
