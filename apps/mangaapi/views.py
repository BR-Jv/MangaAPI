from rest_framework import viewsets
from .models import Manga

class MangasviewSet(viewsets.ModelViewSet):
    """
        Endpoit da API que permite a visualização do catalogo de mangás disponivel.
    """

    mangas = Manga.objects.all().order_by('cadastrado')
    
    
    
    
