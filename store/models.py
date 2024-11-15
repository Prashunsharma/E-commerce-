from django.db import models
import datetime

class Category(models.Model) :
  name=models.CharField(max_length=50)
  def _str_(self):
     return  self.name
 
  class Meta :
    verbose_name_plural='categories'
 

class Customer(models.Model) : 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    def _str_ (self):
         return f'{self.first_name} {self.last_name}'



class Product (models.Model) :
   name=models.CharField(max_length=50)
   price=models.PositiveBigIntegerField(default=0,blank=False)
   category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
   description=models.CharField(max_length=250,default='',blank=True,null=True)
   image=models.ImageField(upload_to='uploads/product/')
   
   
   def _str_(self):
      return self.name
   


class Order(models.Model) : 
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   quantity=models.IntegerField(default=1)
   address=models.CharField(max_length=100,default='',blank=True)
   phone=models.IntegerField(max_length=12,default='',blank=True)
   date=models.DateField(default=datetime.datetime.today)
   status=models.BooleanField(default=False)
   def _str_(self):
      return self.product


