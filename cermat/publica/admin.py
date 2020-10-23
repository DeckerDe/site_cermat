from django.contrib import admin
from .models import Publica, Project

@admin.register(Publica, Project)

class PublicaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status',)




