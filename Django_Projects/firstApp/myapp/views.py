from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse
from datetime import datetime
# Create your views here.


# Data Source 
data = {
    "phone":["Samsung s22","Iphone x","Oppo"],
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
    list_items = ""
    category_list = list(data.keys())
    return render(request,'index.html',{
        "categories":category_list
    })

def electronicPage(request):
    list_item = list(electronicData.values())
    return render(request,"Electronics.html",{
        "electronic":electronicData
    })



# http://127.0.0.1:8000/products/details/
def details(request):
    return HttpResponse("details")

# http://127.0.0.1:8000/products/{1,2,3...}
def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list) or category_id <=0:
        return HttpResponseNotFound("<h5>Invalid Category selection :(</h5>")
    
    category_Name = category_list[category_id-1]
   
    redirect_Path = reverse("products_by_category",args=[category_Name])
    return redirect(redirect_Path)

# http://127.0.0.1:8000/products/{phone,computer,electronic}
def getProductsByCategory(request, category):
    try:
        products = data[category]     
        return render(request,"products.html",{
            "category":category,
            "products":products,
            "now":datetime.now
        })
    except:
        return HttpResponseNotFound('<h1>Incorrect Category</h1>')