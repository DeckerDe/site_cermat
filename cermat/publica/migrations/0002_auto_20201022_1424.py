# Generated by Django 3.1.1 on 2020-10-22 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=250, unique_for_date='start')),
                ('start', models.DateField()),
                ('status', models.CharField(choices=[('Em andamento', 'em andamento'), ('Finalizado', 'finalizado')], max_length=50)),
                ('nature', models.CharField(choices=[('Pesquisa', 'pesquisa'), ('Desenvolvimento', 'desenvolvimento'), ('Extensão', 'extensão')], max_length=50)),
                ('grad', models.PositiveIntegerField()),
                ('mest', models.PositiveIntegerField()),
                ('doc', models.PositiveIntegerField()),
                ('members', models.CharField(max_length=1000)),
                ('funders', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='area',
        ),
        migrations.AddField(
            model_name='post',
            name='sec_author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publica_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='proj',
            field=models.ForeignKey(default='11000', on_delete=django.db.models.deletion.CASCADE, to='publica.project'),
        ),
    ]
