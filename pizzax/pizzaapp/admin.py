from django.contrib import admin

# Register your models here.

from .models import PizzaModel, CustomerModel ,OrderModel

admin.site.register(PizzaModel)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)