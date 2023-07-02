from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product, Order
from .Serializer import ProductSerializer, OrderSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

def index(req):
    return JsonResponse('hello', safe=False)

def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

@api_view(['POST'])
def register(request):
        user = User.objects.create_user(username= request.data["username"],password=request.data['password'],is_staff=1,is_superuser=1)
        return Response({"reg":"test"})

class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart_items = request.data
        print(cart_items)
        serializer = CartItemSerializer(data=request.data,  context={'user': request.user},many=True)
        if serializer.is_valid():
            cart_items = serializer.save()
        #     # Process the cart items as needed
        #     # ...
            return Response("Cart items received and processed successfully.")
        else:
            return Response(serializer.errors, status=400)
    def get(self, request):
        user = request.user
        my_model = user.order_set.all()
        serializer = CartItemSerializer(my_model, many = True)
        return Response(serializer.data)
    
class ProductViewSet(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','post'])
def orders(request):
    all_orders=OrderSerializer(Order.objects.all(),many=True).data
    return Response ( all_orders)


def index(req):
    return HttpResponse('<h1>hello')


def about(req):
    return JsonResponse(f'about', safe=False)

def contact(req):
    return JsonResponse(f'contact', safe=False)