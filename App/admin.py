from django.contrib import admin
from .models.product import Product
from .models.customer import Customer
from .models.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','description','category']
    

class AdminCategory(admin.ModelAdmin):
    list_display = ['name'] 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
