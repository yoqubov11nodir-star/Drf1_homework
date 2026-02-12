from django.urls import path
from .views import get_info, create_product

urlpatterns = [
    path('get-info/', get_info),
    path('create/', create_product)
]