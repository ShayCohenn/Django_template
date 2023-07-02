from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'desc', 'price', 'amount']   
           
        def create(self, validated_data):
            user = self.context['user']
            validated_data['user'] = user
            return Order.objects.create(**validated_data,user=user)

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  ['amount', 'desc', 'price']
    def create(self, validated_data):
        # return Order.objects.create(**validated_data)
        user = self.context['user']
        return Order.objects.create(**validated_data,user=user)