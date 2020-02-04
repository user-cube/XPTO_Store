import datetime

from django.db import models


# Create your models here.

class Items(models.Model):
    titulo = models.CharField(max_length=70)
    picture = models.ImageField(
        upload_to='app/static/img/item/' + str(hash(datetime.datetime.now())) + "/",
        default='app/static/img/default_item.jpg')
    descricao = models.CharField(max_length=5000)
    short = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    quantidade = models.IntegerField(default=0)

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


class wishlist(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Encomenda(models.Model):
    data = models.DateField(auto_now=True)
    produtos = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.id.__str__()

class Email(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.id.__str__()