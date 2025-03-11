from django.db import models


DEMO_CHOICES = [
    ("SN", "Shounen"),
    ("SJ", "Shoujo"),
    ("SE", "Seinen"),
    ("JO", "Josei"),
]

class Manga(models.Model):
    cadastrado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255) 
    volume = models.IntegerField() #! verificar validations 
    capitulo = models.IntegerField() #! verificar validations
    demografia = models.CharField(choices=DEMO_CHOICES, max_length=7)
    

    class meta: 
        ordering = ['cadastrado']

class Mangaka(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)

    class meta: 
        ordering = ['sobrenome']
