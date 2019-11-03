from django.contrib import admin

# Register your models here.
from app.models import Items, Profile, wishlist, Encomenda

admin.site.register(Items)
admin.site.register(Profile)
admin.site.register(wishlist)
admin.site.register(Encomenda)

# Encomenda.objects.all().delete()