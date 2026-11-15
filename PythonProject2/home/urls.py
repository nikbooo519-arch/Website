from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/suv/', views.category_suv, name='category_suv'),
    path('cars/sedan/', views.category_sedan, name='category_sedan'),
    path('cars/coupe/', views.category_coupe, name='category_coupe'),
    path('cars/cabriolet/', views.category_cabriolet, name='category_cabriolet'),
    path('cars/wagon/', views.category_wagon, name='category_wagon'),
    path('cars/hatchback/', views.category_hatchback, name='category_hatchback'),
]