from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET', ])
def get_info(request):
    data = {
        'success': True,
        'message': 'Hammasi yaxshi'
    }
    return Response(data)

@api_view(['POST', ])
def create_product(request):
    serializer = ProductSerializer(data = request.data, files=request.FILES)
    if serializer.is_valid():
        serializer.save()

        data = {
            'success':True,
            'message': 'Maxsulot yaratildi',
            'date': serializer.data
        }
        return Response(serializer.data)
    raise ValidationError(serializer.errors)

@api_view(['GET', ])
def list_product(request):
    products = Product.objects.all()[::-1]
    if len(products) == 0:
        raise ValueError('Malumot yoq')
    serializer = ProductSerializer(products, many=True)

    date = {
        'success':True,
        'massage': 'Product',
        'date': serializer.data
    }
    return Response(serializer.data)


@api_view(['GET', ])
def detail_product(request, pk):
    product = Product.objects.get(pk=pk).first()
    if product is None:
        raise ValueError('Malumot topilmadi')
    serializer = ProductSerializer(product)

    date = {
        'success':True,
        'massage': 'Product',
        'date': serializer.data
    }
    return Response(serializer.data)


@api_view(['PATCH', ])
def patch_product(request, pk):
    product = Product.objects.get(pk=pk).first()
    serializer = ProductSerializer(product, data = request.data)

    if serializer.is_valid():
        serializer.save()

        data = {
            'success':True,
            'message': 'Maxsulot yaratildi',
            'date': serializer.data
        }
        return Response(serializer.data)
    raise ValidationError(serializer.errors)

@api_view(['DELETE', ])
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete() 

    data = {
        'success': True,
        'message': 'Maxsulot ochchirildi'
    }
    return Response(data)