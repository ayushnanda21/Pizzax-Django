from django.contrib import admin

# Register your models here.

from .models import PizzaModel, CustomerModel

admin.site.register(PizzaModel)
admin.site.register(CustomerModel)