from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer

@api_view(['GET', ])
def get_info(request):
    data = {
        'success': True,
        'massage': 'Hammasi yaxshi'
    }
    return Response(data)

@api_view(['POST', ])
def create_product(request):
    serializer = ProductSerializer(date = request.data)
    if serializer.is_valid():
        serializer.save()

        date = {

        }
        return Response(serializer.data)