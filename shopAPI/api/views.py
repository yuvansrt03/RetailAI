from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer,TransactionsSerializer,ShopSerializer
@api_view(['GET'])
def getProducts(request):
    data=Product.objects.all()
    print(data)
    serializer=ProductSerializer(data,many=True)
    return Response(serializer.data)