from rest_framework import serializers
from .models import Manga, Mangaka

class MangasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manga
        fields = ["nome", "volume", "capitulo", "demografia"]


class MangakasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mangaka
        fields = ["nome", "sobrenome"]