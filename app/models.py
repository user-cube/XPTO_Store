import datetime

from django.db import models

# Create your models here.
from django.http import request


class Items(models.Model):
    titulo = models.CharField(max_length=70)
    image = models.CharField(max_length=150)
    descricao = models.CharField(max_length=5000)
    short = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo


class Profile(models.Model):
    nome = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='app/static/img/profile_pictures/' + str(hash(datetime.datetime.now())) + "/",
        default='app/static/img/default.jpg')
    morada = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    pais = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
