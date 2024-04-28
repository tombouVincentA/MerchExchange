from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000, null=True)
    year_formed = models.fields.IntegerField(
            validators=[MinValueValidator(1900), MaxValueValidator(2021)]
        )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    # like_new = models.fields.BooleanField(default=False) <-- SUPPRIMER CETTE LIGNE

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    
    class Type(models.TextChoices):
        DISQUES = 'Records'
        VETEMENTS = 'Clothing'
        AFFICHES = 'Posters'
        DIVERS = 'Miscellaneous'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300, null=True)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)], null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=30, default='Records')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'