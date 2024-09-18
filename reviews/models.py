from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

class Review(models.Model):
    movie =models.ForeignKey(
        Movie, on_delete=models.PROTECT,
        related_name='reviews'
        )

    stars = models.IntegerField(
        validators=[
            #O Validator MinValueValidator e MaxValueValidator são usados para garantir um valor mínimo e máximo para um campo.
            MinValueValidator(0, message='0 é o menor valor possível'),
            MaxValueValidator(5, message='5 é o maior valor possível')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie.title} - {self.stars}'
