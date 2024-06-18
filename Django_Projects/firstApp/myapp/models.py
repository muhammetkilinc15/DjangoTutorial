from django.db import models
from django.utils.text import slugify # For save method
# Create your models here.


# Category Model
class Category(models.Model):
    Name = models.CharField(max_length=100)
 
    # Özelliştirilmiş Verileri döndüren method
    def __str__(self):
        return f"{self.Name}"


# Product Model
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=200)
    ImageUrl = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name="products")
    slug = models.SlugField(default="",blank=True,null=False,db_index=True,unique=True)

    # Özelliştirilmiş Verileri döndüren method
    def __str__(self):
        return f"{self.Name} {self.Price} {self.description}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super().save(*args, **kwargs)

