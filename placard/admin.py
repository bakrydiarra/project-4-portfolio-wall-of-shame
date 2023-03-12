from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Persona)
class PersonaAdmin(SummernoteModelAdmin):
    list_display = ('shamefull_nickname', 'slug', 'created_on')
    search_fields = ['shamefull_nickname', 'shameful_story']
    prepopulated_fields = {'slug': ('shamefull_nickname',)}
    list_filter = ('created_on',)
    summernote_fields = ('shameful_story')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'persona', 'created_on')
    list_filter = ('author', 'created_on')
    search_fields = ('author', 'content')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'persona')
    list_filter = ('author',)
