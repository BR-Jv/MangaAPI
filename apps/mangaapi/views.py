from rest_framework import viewsets
from .models import Manga, Mangaka
from .serializers import MangasSerializer, MangakasSerializer

class MangasviewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite a visualização do catalogo de mangás disponivel.
    """

    queryset = Manga.objects.all().order_by('cadastrado')
    serializer_class = MangasSerializer
    
    
class MangakasviewSet(viewsets.ModelViewSet):
    """
        API endpoint que permite a visualização do catalogo de mangakas cadastrado.
    """
     
    queryset = Mangaka.objects.all().order_by('sobrenome')
    serializer_class = MangakasSerializer
