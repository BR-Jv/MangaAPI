from rest_framework import viewsets
from .models import Manga

class MangasviewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite a visualização do catalogo de mangás disponivel.
    """

    queryset = Manga.objects.all().order_by('cadastrado')
    
    
    
    
