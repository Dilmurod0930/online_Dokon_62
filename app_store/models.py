from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class  Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_logo = models.ImageField(upload_to='images/categories', default='images/categories/default.jpg')

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']
        db_table = 'categories'



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.FloatField(validators=[MinValueValidator(0.0)])
    product_image = models.ImageField(upload_to='images/products', default='images/products/default.jpg')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name}  {self.product_price} {self.product_owner}"

    class Meta:
        ordering = ['product_name']
        db_table = 'products'