from django.db import models
from django.utils.text import slugify # For save method
# Create your models here.


# Category Model
class Category(models.Model):
    Name = models.CharField(max_length=100)
 
    # Özelliştirilmiş Verileri döndüren method
    def __str__(self):
        return f"{self.Name}"


class Adress(models.Model):
    Street = models.CharField(max_length=100)
    Postal_Code = models.CharField(max_length=5)
    City = models.CharField(max_length=30)
   
    def  __str__(self):
       return f"{self.Street} {self.City} {self.Postal_Code}"
    

class Supplier(models.Model):
    Company_Name = models.CharField(max_length=50)
    Adress = models.OneToOneField(Adress,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.Company_Name}"
    


# Product Model
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=200)
    ImageUrl = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True,unique=True)
    Category = models.ManyToManyField(Category)
    Supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    # Özelliştirilmiş Verileri döndüren method
    def __str__(self):
        return f"{self.Name} {self.Price} {self.description}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super().save(*args, **kwargs)

