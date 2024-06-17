from django.db import models

# Create your models here.

# Product Model
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=200)
    ImageUrl = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    Category = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f"{self.Name} {self.Price} {self.description}"
    
    
    