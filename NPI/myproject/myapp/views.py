from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
  

@api_view(['POST'])
def post_category(request):

    if request.method == 'POST':
        category = CategorySerializer(data=request.data)

        if category.is_valid():  # Check if data is valid according to the serializer
            category.save()  
            return Response(category.data, status=status.HTTP_201_CREATED)  
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['POST'])
def post_product(request):

    if request.method == 'POST':
        product = ProductSerializer(data=request.data)

        if product.is_valid():  # Check if data is valid according to the serializer
            product.save()  
            return Response(product.data, status=status.HTTP_201_CREATED)  
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
def get_category(request):
    if request.method=='GET':
        category=Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def get_product(request):
    if request.method=='GET':
        category=Product.objects.all()
        serializer = ProductSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    
@api_view(['PATCH'])
def update_product_byid(request,id):
    if request.method=='PATCH':
        pid=Product.objects.get(id=id)
        serializer=ProductSerializer(pid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['DELETE'])
def delete_product_byid(request,id):
    if request.method=='DELETE':
        pid=Product.objects.get(id=id)
        pid.delete()
        return Response("deleted",status=status.HTTP_200_OK)
    


























# @api_view(['GET'])    
# def get_product_byid(request,id):
#     if request.method=='GET':
#         user=Product.objects.get(id=id)
#         serializer=Product_Serializers(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
