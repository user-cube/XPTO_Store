from django.db import models

# Create your models here.

class Items(models.Model):
    titulo = models.CharField(max_length=70)
    image = models.CharField(max_length=150)
    descricao = models.CharField(max_length=500)
    short = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo