from django import forms
from .models import Food, FoodNon, FoodVegan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#CUSTOMER_CATAGORIES = [
    #('student',"Student"),
    #('staff',"Staff"),
    #('general',"General"),
#]
        

class NewUserForm(UserCreationForm,forms.Form):  


    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]



