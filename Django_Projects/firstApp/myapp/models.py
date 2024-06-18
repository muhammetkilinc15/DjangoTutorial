from django.db import models
from django.utils.text import slugify # For save method
# Create your models here.

# Product Model
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=200)
    ImageUrl = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    Category = models.CharField(max_length=50,null=True)
    slug = models.SlugField(default="",null=False,db_index=True,unique=True)
    
    # slugify ile slug alanına Samsung S 22 degil de Samsung-S-22 yazilacak 
    def save(self, *args,**kargs):
        self.slug= slugify(self.Name)
        super().save(args,kargs)
    
    def __str__(self):
        return f"{self.Name} {self.Price} {self.description}"
    
    
    