from django.core.management.base import BaseCommand, CommandError
from apps.mangaapi.models import Manga



class Command(BaseCommand): 
    help = "Criando dados e enserindo SQLITE para teste de API"

    def handle(self, *args, **options):
    
        m = Manga.objects.create(
            nome = "Akira",
            volume = 6,
            capitulo = 120,
            demografia =  "Seinen",
        )

        m.save()

        self.stdout.write( self.style.SUCCESS('Criação de dados efetuado com sucesso.'))
    