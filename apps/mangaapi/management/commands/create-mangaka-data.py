from django.core.management.base import BaseCommand
from apps.mangaapi.models import Mangaka


class Command(BaseCommand):
    help = "Criando dados e enserindo SQLITE para teste de API"

    def handle(self, *args, **options):

        mangakaContentList = [
            {
                "nome": "Katsuhiro",
                "sobrenome": "Otomo",
            },
            {
                "nome": "Kentaro",
                "sobrenome": "Miura",
            },
            {
                "nome": "Tite",
                "sobrenome": "Kubo",
            },
            {
                "nome": "CLAMP",
                "sobrenome": " ",
            },
            {
                "nome": "Tatsuki",
                "sobrenome": "Fujimoto",
            },
            {
                "nome": "Tsugumi",
                "sobrenome": "Ohba",
            },
                {
                "nome": "Takeshi",
                "sobrenome": "Obata",
            },
            {
                "nome": "Koyoharu",
                "sobrenome": "Gotouge",
            },
            {
                "nome": "Fujiko",
                "sobrenome": "F. Fujio",
            },
            {
                "nome": "Akira",
                "sobrenome": "Toriyama",
            },
            {
                "nome": "Hiromu",
                "sobrenome": "Arakawa",
            },
            {
                "nome": "Natsuki",
                "sobrenome": "Takaya",
            },
            {
                "nome": "Masamune",
                "sobrenome": "Shirow",
            },
            {
                "nome": "Yoshihiro",
                "sobrenome": "Togashi",
            },
            {
                "nome": "Gege",
                "sobrenome": "Akutami",
            },
            {
                "nome": "Tomohito",
                "sobrenome": "Oda",
            },
            {
                "nome": "Kohei",
                "sobrenome": "Horikoshi",
            },
            {
                "nome": "Ai",
                "sobrenome": "Yazawa",
            },
            {
                "nome": "Masashi",
                "sobrenome": "Kishimoto",
            },
            {
                "nome": "Yoshiyuki",
                "sobrenome": "Sadamoto",
            },
                {
                "nome": "Hideaki",
                "sobrenome": "Anno",
            },
            {
                "nome": "Eiichiro",
                "sobrenome": "Oda",
            },
            {
                "nome": "Ai",
                "sobrenome": "Yazawa",
            },
            {
                "nome": "Hidenori",
                "sobrenome": "Kusaka",
            },
            {
                "nome": "Mato",
                "sobrenome": "",
            },
            {
                "nome": "Satoshi",
                "sobrenome": "Yamamoto",
            },
            {
                "nome": "Naoko",
                "sobrenome": "Takeuchi",
            },
            {
                "nome": "Takehiko",
                "sobrenome": "Inoue",
            },
            {
                "nome": "Tatsuya",
                "sobrenome": "Endo",
            },
            {
                "nome": "Kaiu",
                "sobrenome": "Shirai",
            },
                {
                "nome": "Posuka",
                "sobrenome": "Demizu",
            },
            {
                "nome": "Sui",
                "sobrenome": "Ishida",
            },
            {
                "nome": "Takehiko",
                "sobrenome": "Inoue",
            },
            {
                "nome": "Makoto",
                "sobrenome": "Yukimura",
            },
            {
                "nome": "Naoshi",
                "sobrenome": "Arakawa",
            }
        ]

        mangakaObjects=[]
        for content in mangakaContentList:
            mangakaObjects.append(Mangaka(nome=content["nome"], sobrenome=content["sobrenome"]))
        
        try: 
            Mangaka.objects.bulk_create(mangakaObjects)
            self.stdout.write(self.style.SUCCESS('Criação de dados efetuado com sucesso.'))
        except: 
            self.stdout.write(self.style.DANGER('Criação de dados falhou, verifique o código.'))

    