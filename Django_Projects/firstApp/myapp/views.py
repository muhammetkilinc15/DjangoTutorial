from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.


# Data Source 
data = {
    "phone":"telefon kategorisindeki ürünler",
    "computer":"bilgisayar kategorisindeki ürünler",
    "electronic":"elektronik kategorisindeki ürünler"
}


# http://127.0.0.1:8000/products/
def index(request):
    return HttpResponse("index Page")

# http://127.0.0.1:8000/products/details/
def details(request):
    return HttpResponse("details")

# http://127.0.0.1:8000/products/{1,2,3...}
def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list) or category_id <=0:
        return HttpResponseNotFound("Invalid Category selection :(")
    redirect_text = category_list[category_id-1]
    return HttpResponseRedirect("/products/" + redirect_text)

# http://127.0.0.1:8000/products/{phone,computer,electronic}
def getProductsByCategory(request, category):
    try:
        category_text = data[category]        
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('Incorrect Category')