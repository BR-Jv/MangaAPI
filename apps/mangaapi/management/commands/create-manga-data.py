from django.core.management.base import BaseCommand, CommandError
from apps.mangaapi.models import Manga


class Command(BaseCommand):
    help = "Criando dados e enserindo SQLITE para teste de API"

    def handle(self, *args, **options):

        mangasContentList = [
            {
                "nome" : "Berserk",
                "volume" : 41,
                "capitulo" : 364,
                "demografia" : "Seinen",
            },
            {
                "nome" : "Bleach",
                "volume" : 74,
                "capitulo" : 686,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Cardcaptor Sakura",
                "volume" : 12,
                "capitulo" : 50,
                "demografia" : "Shoujo",
            },
            {
                "nome" : "Chainsaw Man",
                "volume" : 11,
                "capitulo" : 97,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Death Note",
                "volume" : 12,
                "capitulo" : 108,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Demon Slayer : Kimetsu no Yaiba",
                "volume" : 23,
                "capitulo" : 205,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Doraemon",
                "volume" : 45,
                "capitulo" : 1344,
                "demografia" : "Kodomo",
            },
            {
                "nome" : "Dragon Ball",
                "volume" : 42,
                "capitulo" : 519,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Fullmetal Alchemist",
                "volume" : 27,
                "capitulo" : 108,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Fruits Basket",
                "volume" : 23,
                "capitulo" : 136,
                "demografia" : "Shoujo",
            },
            {
                "nome" : "Ghost in the Shell",
                "volume" : 2,
                "capitulo" : 35,
                "demografia" : "Seinen",
            },
            {
                "nome" : "Hunter x Hunter",
                "volume" : 37,
                "capitulo" : 390,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Jujutsu Kaisen",
                "volume" : 25,
                "capitulo" : 230,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Komi Can't Communicate",
                "volume" : 32,
                "capitulo" : 409,
                "demografia" : "Shounen",
            },
            {
                "nome" : "My Hero Academia",
                "volume" : 37,
                "capitulo" : 387,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Nana",
                "volume" : 21,
                "capitulo" : 84,
                "demografia" : "Josei",
            },
            {
                "nome" : "Naruto",
                "volume" : 72,
                "capitulo" : 700,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Neon Genesis Evangelion",
                "volume" : 14,
                "capitulo" : 97,
                "demografia" : "Seinen",
            },
            {
                "nome" : "One Piece",
                "volume" : 107,
                "capitulo" : 1085,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Paradise Kiss",
                "volume" : 5,
                "capitulo" : 36,
                "demografia" : "Josei",
            },
            {
                "nome" : "Pokémon Adventures",
                "volume" : 64,
                "capitulo" : 650,
                "demografia" : "Kodomo",
            },
            {
                "nome" : "Sailor Moon",
                "volume" : 18,
                "capitulo" : 52,
                "demografia" : "Shoujo",
            },
            {
                "nome" : "Slam Dunk",
                "volume" : 31,
                "capitulo" : 276,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Spy x Family",
                "volume" : 11,
                "capitulo" : 80,
                "demografia" : "Shounen",
            },
            {
                "nome" : "The Promised Neverland",
                "volume" : 20,
                "capitulo" : 181,
                "demografia" : "Shounen",
            },
            {
                "nome" : "Tokyo Ghoul",
                "volume" : 14,
                "capitulo" : 143,
                "demografia" : "Seinen",
            },
            {
                "nome" : "Vagabond",
                "volume" : 37,
                "capitulo" : 327,
                "demografia" : "Seinen",
            },
            {
                "nome" : "Vinland Saga",
                "volume" : 26,
                "capitulo" : 205,
                "demografia" : "Seinen",
            },
            {
                "nome" : "Your Lie in April",
                "volume" : 11,
                "capitulo" : 44,
                "demografia" : "Shounen",
            }
        ]

        mangasObjects=[]
        for content in mangasContentList:
            mangasObjects.append(Manga(nome=content["nome"], volume=content["volume"], capitulo=content["capitulo"], demografia=content["demografia"]))
        
        try: 
            Manga.objects.bulk_create(mangasObjects)
            self.stdout.write(self.style.SUCCESS('Criação de dados efetuado com sucesso.'))
        except: 
            self.stdout.write(self.style.DANGER('Criação de dados falhou, verifique o código.'))

    