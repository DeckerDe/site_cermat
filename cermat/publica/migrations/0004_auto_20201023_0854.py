# Generated by Django 3.1.1 on 2020-10-23 11:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publica', '0003_auto_20201023_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Publica',
        ),
    ]
