from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# localhost:
def index (request):
    return HttpResponse("Muhammet Kilinç")


def details(request):
    return HttpResponse("detais")

def list(request):
    return HttpResponse("list")