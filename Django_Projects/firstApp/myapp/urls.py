from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index),
    path('<int:id>', views.details, name='details'),
    path('electronicPage', views.electronicPage, name='electronicPage'),
    path('<int:category_id>', views.getProductsByCategoryId),
    path('<str:category>', views.getProductsByCategory,name='products_by_category')
]