from django.db import models

#Como boa prática em Python, é recomendado que as constantes sejam definidas em letras maiúsculas
#Esse é o choices para a nacionalidade do ator
NATIONALITY_CHOICES = (
    ('BRA', 'Brasileira'),
    ('USA', 'Americana'),
    ('FRA', 'Francesa'),
    ('ITA', 'Italiana'),
    ('JPN', 'Japonesa'),
    ('KOR', 'Coreana'),
    ('CHN', 'Chinesa'),
    ('IND', 'Indiana'),
    ('RUS', 'Russa'),
    ('AUS', 'Australiana'),
    ('CAN', 'Canadense'),
    ('MEX', 'Mexicana'),
    ('ARG', 'Argentina'),
    ('COL', 'Colombiana'),
    ('PER', 'Peruana'),
    ('VEN', 'Venezuelana'),
    ('CHL', 'Chilena'),
    ('URY', 'Uruguaia'),
    ('ESP', 'Espanhola'),
    ('POR', 'Portuguasa'),
    ('GBR', 'Britânica'),
    ('DEU', 'Alemã'),
    ('NLD', 'Holandesa'),
    ('BEL', 'Belga'),
    ('SWE', 'Sueca'),
    ('NOR', 'Norueguesa'),
    ('FIN', 'Finlandesa'),
    ('DNK', 'Dinamarquesa'),
    ('POL', 'Polonesa'),
    ('CZE', 'Tcheca'),
    ('HUN', 'Húngara'),
    ('TUR', 'Turca'),
    ('GRC', 'Grega'),
    ('EGY', 'Egípcia'),
    ('ZAF', 'Sul-africana'),
    ('NGA', 'Nigeriana'),
    ('KEN', 'Queniana'),
    ('ETH', 'Etíope'),
    ('MAR', 'Marroquina'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name
    