from django.contrib import admin

# Register your models here.
from app.models import Items, Profile

admin.site.register(Items)
admin.site.register(Profile)
