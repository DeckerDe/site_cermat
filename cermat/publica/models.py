from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='publicado')

class Project(models.Model):
    PROJ_STATUS = (
        ('Em andamento', 'em andamento'),
        ('Finalizado', 'finalizado')
    )

    NAT_CHOICES = (
        ('Pesquisa', 'pesquisa'),
        ('Desenvolvimento', 'desenvolvimento'),
        ('Extensão', 'extensão')
    )

    title = models.CharField(max_length=255)
    body = models.TextField(default='Projeto sem descrição')
    slug = models.SlugField(max_length=250, unique_for_date='start')
    start = models.DateField()
    status = models.CharField(max_length=50, choices=PROJ_STATUS)
    nature = models.CharField(max_length=50, choices=NAT_CHOICES)
    grad = models.PositiveIntegerField()
    mest = models.PositiveIntegerField()
    doc = models.PositiveIntegerField()
    members = models.CharField(max_length=1000)
    funders = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Publica(models.Model):
    objects = models.Manager() #Default manager
    published = PublishedManager() #Custom manager
    STATUS_CHOICES  = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=250, unique=True)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE, default='11000')
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True)
    author = models.ForeignKey(User, related_name='publica_posts', on_delete=models.PROTECT)
    sec_author = models.ManyToManyField(User)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'publica:publica_detalhe',
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug])




