from django.urls import path
from . import views
urlpatterns = {
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('details',views.details,name='details'),
    path('list',views.list,name='list')
}