from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.shortcuts import redirect,render
from django.urls import reverse
from datetime import datetime
from myapp.models import Product
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.urls import path

# Create your views here.


# Data Source 
data = {
    "phone":["Samsung s22","Iphone x","Oppo","Iphone 15 Pro"],
    "computer":["Monster","MSI","Asus"],
    "electronic":[]
}


electronicData = {
    "computer":["Monster","Macbook","Samsung"],
    "phone" : ["Iphone","Xamio","Oppo"],
    "keyboards": ["Monster","Regex"]
}

# http://127.0.0.1:8000/products/
def index(request):
    products = Product.objects.filter(isActive=True). order_by("-Price")
    productCount = Product.objects.count()
    avg_price = Product.objects.filter(isActive=True).aggregate(Avg("Price"))
    return render(request,'index.html',{
        "products":products,
        "ProductCount":productCount,
        "Avg_Price":avg_price
    })

def list(request):
    if request.GET['q'] and request.GET['q'] is not None :
        q = request.GET['q']
        products = Product.objects.filter(Name__contains=q).order_by("-Price")
        print(request.GET['q'])
    else :
        products = Product.objects.all().order_by("-Price")
       
    
    context = {
        "products":products
    }   
    
    return render(request,"list.html",context)


# http://127.0.0.1:8000/products/details/
def details(request,slug):
    product = get_object_or_404(Product,slug=slug)
    context = {
        "product":product
    }
    return render(request,"details.html",context)



def create(request):
    if request.method == 'POST':
        pName = request.POST["Name"]
        Price = request.POST["Price"]
        description = request.POST["description"]
        ImageUrl = request.POST["ImageUrl"]
        slug = request.POST["slug"]
        
        p1 = Product(Name=pName,description=description,Price=Price,ImageUrl=ImageUrl,slug=slug)
        p1.save()
        return redirect("index")
    return render(request,"create.html")

