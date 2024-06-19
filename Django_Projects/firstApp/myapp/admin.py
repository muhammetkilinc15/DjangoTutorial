from django.contrib import admin
from .models import Product ,Category, Adress,Supplier
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # Admin panelinde listede gösterilecek alanlar
    list_display = ("Name",)
    
    # Admin panelinde listedeki öğeler için bağlantı verilecek alanlar
    list_display_links = ("Name",)
    
    # Admin panelinde filtreleme yapılacak alanlar
    list_filter = ("Name",)
    
    # Admin panelinde aranabilir alanlar
    search_fields = ("Name",)



class ProductAdmin(admin.ModelAdmin):
    # Admin panelinde listede gösterilecek alanlar
    list_display = ("Name", "Price","isActive","Categories","Supplier")
    
    # Slug alanını Name alanına göre otomatik doldurmak için prepopulated_fields
    prepopulated_fields = {"slug": ("Name",)}
    
    # Admin panelinde listede linkli gösterilecek  alanlar
    list_display_links = ("Name",)
   
    # Admin panelinde yalnızca okunabilir alanlar
        #readonly_fields = ("slug",)
    
    
    # Admin panelinde filtreleme yapılacak alanlar
    list_filter = ("Name","Category")
    
    # Admin panelinde düzenlenebilir alanlar
    #list_editable = ("isActive",)
    
    # Admin panelinde aranabilir alanlar
    search_fields = ("Name",)
    
    def Categories(self,obj): 
        html = ""
        for categoryy in obj.Category.all():
            html+=categoryy.Name + " - "
        return html

   
    
    

admin.site.register(Supplier)
admin.site.register(Adress)
admin.site.register(Product ,ProductAdmin)
admin.site.register(Category, CategoryAdmin)

