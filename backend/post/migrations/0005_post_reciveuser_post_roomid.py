# Generated by Django 4.2.1 on 2023-06-07 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_post_realname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reciveuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recive_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='roomid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]