from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE , default=1)
    image = models.ImageField(upload_to='products/')
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id = ids)
    
    
    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
        
    