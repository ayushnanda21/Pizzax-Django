from django.contrib import admin

# Register your models here.

from .models import PizzaModel

admin.site.register(PizzaModel)