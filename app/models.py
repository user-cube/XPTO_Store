from django.db import models

# Create your models here.

class Items(models.Model):
    titulo = models.CharField(max_length=70)
    image = models.CharField(max_length=150)
    descricao = models.CharField(max_length=5000)
    short = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo

class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(null=False, max_length=50)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    unitValue = models.DecimalField(max_digits=11, decimal_places=2, default=1)
    total = models.DecimalField(max_digits=11, decimal_places=2, default=1)

    def __str__(self):
        return self.autor