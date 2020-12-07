# Generated by Django 3.1.1 on 2020-11-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publica', '0009_remove_publica_sec_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('researchgate', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('lattes', models.URLField(blank=True)),
            ],
        ),
    ]
