from django.contrib import admin

# Register your models here.
from app.models import Items, Carrinho

admin.site.register(Items)
admin.site.register(Carrinho)