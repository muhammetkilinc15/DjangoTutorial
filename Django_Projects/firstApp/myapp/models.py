from django.db import models

# Create your models here.

# Product Model
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=200)
    ImageUrl = models.CharField(max_length=20)
    
    
    