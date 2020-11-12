from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()

class Researcher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    organization = models.CharField(max_length=255)
    organization_abre = models.CharField(max_length=50, blank=True)
    researchgate = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    lattes = models.URLField(blank=True)

    unique_together = ['name', 'organization']

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

    def get_absolute_url(self):
        return reverse(
            'publica:projeto_detalhe',
            args=[self.start.year, self.start.month, self.start.day, self.slug])

class Publica(models.Model):
    objects = models.Manager() #Default manager
    published = PublishedManager() #Custom manager
    STATUS_CHOICES  = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=250, unique=True)
    researchers = models.ManyToManyField(Researcher)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE, default='11000')
    journal = models.CharField(max_length=250, default='Publicação interna')
    url = models.URLField(blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True)
    author = models.ForeignKey(User, related_name='publica_posts', on_delete=models.PROTECT)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Publica, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('publica:editar_publica',
        args=[self.slug])

    def get_absolute_url(self):
        return reverse(
            'publica:publica_detalhe',
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug])





