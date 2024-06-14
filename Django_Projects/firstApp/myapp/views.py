from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


# Data Source 
data = {
    "phone":"telefon kategorisindeki ürünler",
    "computer":"bilgisayar kategorisindeki ürünler",
    "electronic":"elektronik kategorisindeki ürünler"
}


# http://127.0.0.1:8000/products/
def index(request):
    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirect_Path = reverse("products_by_category", args=[category]) #dynamically creates url for us
        list_items += f'<li><a href="{redirect_Path}">{category}</a></li>'
    html = f'<ul>{list_items}</ul>'
    return HttpResponse(html)

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
        category_text = data[category]        
        return HttpResponse(f'<h1>{category_text}</h1>')
    except:
        return HttpResponseNotFound('<h1>Incorrect Category</h1>')