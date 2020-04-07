from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
@api_view(['GET','POST'])

def Product_list(request):
    if request.method=='GET':
        obj=Product.objects.all()
        serializer=ProductSerializer(obj,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
def Product_detail(request,pk):
    try:
        obj=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class Person(APIView):
    def get(self,request,format=None):
        message={
            'Response':200,
            'Message':"welcome to django"
        }
        return Response(message)

