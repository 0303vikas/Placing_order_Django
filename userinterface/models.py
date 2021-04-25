from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now





# model class containing vegetarian food order details
class Food(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="User")   
    food_name = models.CharField(max_length=100, verbose_name="DishName", db_column="Hello")
    food_amount = models.IntegerField(verbose_name="Quantity")
    food_price= models.DecimalField(decimal_places=2,max_digits=7,verbose_name="Price") 
    date_time= models.DateTimeField(default=now,verbose_name="Date-Time")
   

    def __str__(self):
        return str(self.owner) + '       ' + str(self.food_name) 

# model class containing vegan food order details
class FoodVegan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="User")   
    food_name = models.CharField(max_length=100, verbose_name="DishName", db_column="Hello")
    food_amount = models.IntegerField(verbose_name="Quantity")
    food_price= models.DecimalField(decimal_places=2,max_digits=7,verbose_name="Price") 
    date_time= models.DateTimeField(default=now, verbose_name="Date-Time")
   

    def __str__(self):
        return str(self.owner) + '       ' + str(self.food_name) 

# model class containing non vegetarian food order details
class FoodNon(models.Model):    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="User")   
    food_name = models.CharField(max_length=100, verbose_name="DishName", db_column="Hello")
    food_amount = models.IntegerField(verbose_name="Quantity")
    food_price= models.DecimalField(decimal_places=2,max_digits=7,verbose_name="Price") 
    date_time= models.DateTimeField(default=now,verbose_name="Date-Time")
   

    def __str__(self):
        return str(self.owner) + '       ' + str(self.food_name) 










