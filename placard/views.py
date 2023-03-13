from django.shortcuts import render
from django.views import generic
from .models import *


class PersonaList(generic.ListView):
    model = Persona
    queryset = Persona.objects.order_by('created_on')
    template_name = 'persona_details.html'
    paginate_by = 6
