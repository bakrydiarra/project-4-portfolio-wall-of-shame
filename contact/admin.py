from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactForm)
class ContactFormAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'message', 'reason', 'written_on')
    summernote_fields = ('message')
    list_filter = ('name', 'reason', 'written_on')
