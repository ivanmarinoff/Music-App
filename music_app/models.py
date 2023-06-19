from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from .validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), username_validator],
        blank=False,
        null=False,
        verbose_name="Username",
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Email",
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    class Genre(models.TextChoices):
        POP_MUSIC = "Pop Music"
        JAZZ_MUSIC = "Jazz Music"
        R_N_B_MUSIC = "R&B Music"
        ROCK_MUSIC = "Rock Music"
        COUNTRY_MUSIC = "Country Music"
        DANCE_MUSIC = "Dance Music"
        HIP_HOP_MUSIC = "Hip Hop Music"
        OTHER = "Other"


    # CHOICES = [
    #     (POP_MUSIC, POP_MUSIC),
    #     (JAZZ_MUSIC, JAZZ_MUSIC),
    #     (R_N_B_MUSIC, R_N_B_MUSIC),
    #     (ROCK_MUSIC, ROCK_MUSIC),
    #     (COUNTRY_MUSIC, COUNTRY_MUSIC),
    #     (DANCE_MUSIC, DANCE_MUSIC),
    #     (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
    #     (OTHER, OTHER)
    # ]
    album_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), username_validator],
        blank=False,
        null=False,
        unique=True,
        verbose_name="Album name",
    )
    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    genre = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        choices=Genre.choices,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL",
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=False,
        null=False,
    )
