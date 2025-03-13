from rest_framework import serializers
from .models import Manga

class MangasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manga
        fields = ["nome", "volume", "capitulo", "demografia"]