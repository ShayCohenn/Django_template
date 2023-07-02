from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField()
    createdTime=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
           return f'{self.desc} {self.price} '
    
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    createdTime=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
           return f'{self.desc}  '
