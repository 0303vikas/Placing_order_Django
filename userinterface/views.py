import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.views.generic import TemplateView, ListView
from .forms import  NewUserForm, Food, FoodNon, FoodVegan
from django.db.models import Q

from datetime import datetime, timedelta

from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



#Registration class to register new user to the website
class Register(TemplateView):

    # location of template which needs to be displayed
    template_name = "userinterface/register.html"
    
    # get function reades the get request and,
    # displayes the registration page and form
    # if user if alredy authenticated, redirect to home page
    # else display user form from forms.py
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = NewUserForm()
            context = {'form': form}
            return render(request, self.template_name,context)

    # if user post post the regestration form, save the user and redirect to login    
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "User "+ user+ " succesfully created.")
            return redirect('login')
        context = {'form': form}
        return render(request, self.template_name, context)



# Login page
class LoginPage(TemplateView):
    template_name = "userinterface/login.html"

    # method to keep username and user id
    def __init__(self):
        self.username = ""
        self.id = ""
    
    # if the user is authenticated, redirect to home page
    #else render the login page
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        else:              
            context = {}      
            return render(request, self.template_name, context)

    # read the login post form and get the username and password 
    # authenticated the username and password
    # if user exist, log user in and redirect to home page
    # else send authentication failed messages
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)                     
            return redirect('home')
        else:
            if authenticate(request, username=username) is None:
                messages.info(request, "Username doesn't exit.")                
            elif authenticate(request, username=username) is not None:
                messages.info(request, 'Password is incorrect.')
        
        context = {}
        return render(request, self.template_name, context)
    
    #accessors 
    def set_username(self,username):
        self.username = username
        
   
    def set_id(self,id):
        self.id = id
        
    # mutators
    def get_username(self):
        return self.username
    
    def get_id(self):
        return self.id

    # strate returning function
    def __str__(self):
        return "Username: " + str(self.username) + "\nId: " +str(self.id)




#for logging out the user
class Logoutpage(TemplateView):

    def get(self,request):
        logout(request)
        return redirect('login')



# class to display all the food categories 
class Home(ListView,LoginPage):

    # initalizing function 
    def __init__(self):
        super().__init__()
        self.foodtype = "" 
           

    # function to render home page
    def get(self, request):
               
        return render(request,"userinterface/home.html", {}) 

    # accessor and mutator function
    def set_food_type(self, foodtype):
        self.foodtype = foodtype
    
    def get_food_type(self):
        return self.foodtype      

    # printing the state of the class
    def __str__(self):
        return "User name: " + str(self.username)+ "\nUser id: " + str(self.id) + "\nFood category: " + str(self.foodtype)  



# for vegeterian food types
class VegetarianFood(Home):

    # initalizing function
    def __init__(self):
        super().__init__()
        self.food_name = []
        self.food_amount = []
        self.food_price = []
        self.food_order_time = []       
                 
    # page address
    template_name = "userinterface/VegetarianFood.html"        

    # renders the vegetarian food list
    def get(self, request):                     
        return render(request, self.template_name, {})

    # post request to place the order to the user, and save to database
    def post(self, request):

        # calling the function for OOP programming
        # instance of the vegetarinfood
        random = VegetarianFood()

        # Multiple instances of class
        #random1 = VegetarianFood()       
        #random1.set_username("King")
        #random1.set_id("1000")
        #random1.append_food_name("sandwitch")
        #random1.append_food_amount(4)
        #random1.append_food_price(100)
        #random1.append_order_time(datetime.now())           
        #random1.set_food_type("Vegetarian") 
        #print(random1)
        

        # getting username and id from the session and setting it in __init__ function
        user_id = request.user.id
        user_name = request.user.username 
        random.set_username(user_name)
        random.set_id(user_id)

        # select the table of the user who is logged in 
        # if the user post and change in the first vegetarian food type
        # it save the data in the module
        o = request.user       
        model = Food.objects.select_related("owner").filter(owner=o).get(id=1)
        if request.POST.get('input1.0'): 
            model.owner  = request.user                       
            model.food_name =  request.POST.get('input1.0')
            model.food_amount =request.POST.get('input1.1')
            model.food_price = request.POST.get('input1.2')             
            model.date_time =   datetime.now()
            model.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input1.0'))
            random.append_food_amount(request.POST.get('input1.1'))
            random.append_food_price(request.POST.get('input1.2'))
            random.append_order_time(datetime.now())           
                        
            
        # select the table of the user who is logged in 
        # if the user post and change in the second vegetarian food type
        # it save the data in the module
        if request.POST.get('input2.0'): 
            model1 = Food.objects.select_related("owner").filter(owner=o).get(id=2)
            model1.owner  = request.user               
            model1.food_name = request.POST.get('input2.0')
            model1.food_amount = request.POST.get('input2.1')
            model1.food_price = request.POST.get('input2.2')
            model1.date_time = datetime.now()
            model1.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input2.0'))
            random.append_food_amount(request.POST.get('input2.1'))
            random.append_food_price(request.POST.get('input2.2'))
            random.append_order_time(datetime.now())
            
        # select the table of the user who is logged in 
        # if the user post and change in the third vegetarian food type
        # it save the data in the module
        if request.POST.get('input3.0'):
            model2 = Food.objects.select_related("owner").filter(owner=o).get(id=3)
            model2.owner  = request.user                 
            model2.food_name = request.POST.get('input3.0')
            model2.food_amount = request.POST.get('input3.1')
            model2.food_price = request.POST.get('input3.2')
            model2.date_time = datetime.now()
            model2.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input3.0'))
            random.append_food_amount(request.POST.get('input3.1'))
            random.append_food_price(request.POST.get('input3.2'))
            random.append_order_time(datetime.now())
          
        # select the table of the user who is logged in 
        # if the user post and change in the fourth vegetarian food type
        # it save the data in the module
        if request.POST.get('input4.0'):
            model3 = Food.objects.select_related("owner").filter(owner=o).get(id=4)
            model3.owner  = request.user                
            model3.food_name = request.POST.get('input4.0')
            model3.food_amount = request.POST.get('input4.1')
            model3.food_price = request.POST.get('input4.2')
            model3.date_time = datetime.now()
            model3.save()

            # append the saved data in the instance of the class 
            random.food_name.append(request.POST.get('input4.0'))
            random.food_amount.append(request.POST.get('input4.1'))
            random.food_price.append(request.POST.get('input4.2'))
            random.food_order_time.append(datetime.now())
          
        # set food type name in the instance of the class 
        random.set_food_type("Vegetarian") 

        # print the instance of the class vegetarian               
        print(random)
        # redirect to final recipe
        return redirect('finallist')

    # mutators to append the list in the __init__ method
    def append_food_name(self, name):
        self.food_name.append(name)
        

    def append_food_amount(self, amount):
        self.food_amount.append(amount)
        
    
    def append_food_price(self, price):
        self.food_price.append(price)
        
    
    def append_order_time(self, time_o):
        self.food_order_time.append(time_o)

    # mutators of the __init__
    def set_food_name(self, name):
        self.food_name = name
        

    def set_food_amount(self, amount):
        self.food_amount = amount
        
    
    def set_food_price(self, price):
        self.food_price = price
        
    
    def set_order_time(self, time_o):
        self.food_order_time = time_o  

    # accessors of the __init__ method
    def get_food_name(self):
        for i in self.food_name:
            print(i)

    def get_food_amount(self):
        for i in self.food_amount:
            print(i)

    def get_food_price(self):
        for i in self.food_price:
            print(i)

    def get_order_time(self):
        for i in self.food_order_time:
            print(i)

    # print the state of the class vegetarian
    def __str__(self):
        return "\n\nDetails of the order are...\nUser name: "  + str(self.username)+ "\nUser id: " + str(self.id) + "\nFood category: " + str(self.get_food_type())  + "\nFood name: " + str(self.food_name) + "\nFood amount: " + str(self.food_amount) + "\nFood price: " + str(self.food_price) + "\nFood Order time: " + str(self.food_order_time) + "\n"

    


# for nonvegeterian food types
class NonVegFood(Home):

    # page address
    template_name="userinterface/NonVegFood.html"


    # initlizing method to keep the state of the class
    def __init__(self):
        super().__init__()
        self.food_name = []
        self.food_amount = []
        self.food_price = []
        self.food_order_time = []       
                 

    # get method to render the NonVeg food template
    def get(self, request):       
        return render(request, self.template_name, {})


    # post request to place the order to the user, and save to database
    def post(self, request):
        # calling the function for OOP programming
        # instance of the vegetarinfood
        random = NonVegFood()
        

        # getting username and id from the session and setting it in __init__ function        
        user_id = request.user.id
        user_name = request.user.username 
        random.set_username(user_name)
        random.set_id(user_id)

        # select the table of the user who is logged in 
        # if the user post and change in the first non vegetarian food type
        # it save the data in the module
        o = request.user       
        model = FoodNon.objects.select_related("owner").filter(owner=o).get(id=1)
        if request.POST.get('input1.0'): 
            model.owner  = request.user                       
            model.food_name =  request.POST.get('input1.0')
            model.food_amount =request.POST.get('input1.1')
            model.food_price = request.POST.get('input1.2')
            model.date_time = datetime.now()
            model.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input1.0'))
            random.append_food_amount(request.POST.get('input1.1'))
            random.append_food_price(request.POST.get('input1.2'))
            random.append_order_time(datetime.now())
   
        # select the table of the user who is logged in 
        # if the user post and change in the second non vegetarian food type
        # it save the data in the module
        if request.POST.get('input2.0'): 
            model1 = FoodNon.objects.select_related("owner").filter(owner=o).get(id=2)
            model1.owner  = request.user               
            model1.food_name = request.POST.get('input2.0')
            model1.food_amount = request.POST.get('input2.1')
            model1.food_price = request.POST.get('input2.2')
            model1.date_time = datetime.now()
            model1.save() 

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input2.0'))
            random.append_food_amount(request.POST.get('input2.1'))
            random.append_food_price(request.POST.get('input2.2'))
            random.append_order_time(datetime.now())
      

        # select the table of the user who is logged in 
        # if the user post and change in the third non vegetarian food type
        # it save the data in the module
        if request.POST.get('input3.0'):
            model2 = FoodNon.objects.select_related("owner").filter(owner=o).get(id=3)
            model2.owner  = request.user                 
            model2.food_name = request.POST.get('input3.0')
            model2.food_amount = request.POST.get('input3.1')
            model2.food_price = request.POST.get('input3.2')
            model2.date_time = datetime.now()
            model2.save() 

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input3.0'))
            random.append_food_amount(request.POST.get('input3.1'))
            random.append_food_price(request.POST.get('input3.2'))
            random.append_order_time(datetime.now())
          

        # select the table of the user who is logged in 
        # if the user post and change in the fourth non vegetarian food type
        # it save the data in the module
        if request.POST.get('input4.0'):
            model3 = FoodNon.objects.select_related("owner").filter(owner=o).get(id=4)
            model3.owner  = request.user                
            model3.food_name = request.POST.get('input4.0')
            model3.food_amount = request.POST.get('input4.1')
            model3.food_price = request.POST.get('input4.2')
            model3.date_time = datetime.now()
            model3.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input4.0'))
            random.append_food_amount(request.POST.get('input4.1'))
            random.append_food_price(request.POST.get('input4.2'))
            random.append_order_time(datetime.now())
                  

        # set food type name in the instance of the class 
        random.set_food_type("Non-Vegetarian")

        # print the instance of the class vegetarian               
        print(random)
        # redirect to final recipe
        return redirect('finallist')

    # mutators to append the list in the __init__ method
    def append_food_name(self, name):
        self.food_name.append(name)
        

    def append_food_amount(self, amount):
        self.food_amount.append(amount)
        
    
    def append_food_price(self, price):
        self.food_price.append(price)
        
    
    def append_order_time(self, time_o):
        self.food_order_time.append(time_o)

    # mutators of method __init__   
    def set_food_name(self, name):
        self.food_name = name
        

    def set_food_amount(self, amount):
        self.food_amount = amount
        
    
    def set_food_price(self, price):
        self.food_price = price
        
    
    def set_order_time(self, time_o):
        self.food_order_time = time_o  

    # accessors of method __init__
    def get_food_name(self):
        for i in self.food_name:
            print(i)

    def get_food_amount(self):
        for i in self.food_amount:
            print(i)

    def get_food_price(self):
        for i in self.food_price:
            print(i)

    def get_order_time(self):
        for i in self.food_order_time:
            print(i)

    # print the state of the class
    def __str__(self):
        return "\n\nDetails of the order are...\nUser name: "  + str(self.username)+ "\nUser id: " + str(self.id) + "\nFood category: " + str(self.get_food_type())  + "\nFood name: " + str(self.food_name) + "\nFood amount: " + str(self.food_amount) + "\nFood price: " + str(self.food_price) + "\nFood Order time: " + str(self.food_order_time) + "\n"


    

    

# for vegan food types
class VeganFood(Home):

    # contains the address of the vegan page
    template_name="userinterface/VeganFood.html"

    # initlizing method to keep the state of the class
    def __init__(self):
        super().__init__()
        self.food_name = []
        self.food_amount = []
        self.food_price = []
        self.food_order_time = []       
                 
                  
        
    # get method to render the NonVeg food template
    def get(self, request):        
        return render(request, self.template_name, {})

    # post request to place the order to the user, and save to database
    def post(self, request):

         # calling the function for OOP programming
        # instance of the vegetarinfood 
        random = VeganFood() 

        # getting username and id from the session and setting it in __init__ function  
        user_id = request.user.id
        user_name = request.user.username 
        random.set_username(user_name)
        random.set_id(user_id)

         # select the table of the user who is logged in 
        # if the user post and change in the first vegenfood type
        # it save the data in the module
        o = request.user       
        model = FoodVegan.objects.select_related("owner").filter(owner=o).get(id=1)
        if request.POST.get('input1.0'): 
            model.owner  = request.user                       
            model.food_name =  request.POST.get('input1.0')
            model.food_amount =request.POST.get('input1.1')
            model.food_price = request.POST.get('input1.2')
            model.date_time = datetime.now()
            model.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input1.0'))
            random.append_food_amount(request.POST.get('input1.1'))
            random.append_food_price(request.POST.get('input1.2'))
            random.append_order_time(datetime.now())                  
           
            
          # select the table of the user who is logged in 
        # if the user post and change in the second vegen food type
        # it save the data in the module   
        if request.POST.get('input2.0'): 
            model1 = FoodVegan.objects.select_related("owner").filter(owner=o).get(id=2)
            model1.owner  = request.user               
            model1.food_name = request.POST.get('input2.0')
            model1.food_amount = request.POST.get('input2.1')
            model1.food_price = request.POST.get('input2.2')
            model1.date_time = datetime.now()
            model1.save()

            # append the saved data in the instance of the class  
            random.append_food_name(request.POST.get('input2.0'))
            random.append_food_amount(request.POST.get('input2.1'))
            random.append_food_price(request.POST.get('input2.2'))
            random.append_order_time(datetime.now())    
            

         # select the table of the user who is logged in 
        # if the user post and change in the thrid vegan food type
        # it save the data in the module
        if request.POST.get('input3.0'):
            model2 = FoodVegan.objects.select_related("owner").filter(owner=o).get(id=3)
            model2.owner  = request.user                 
            model2.food_name = request.POST.get('input3.0')
            model2.food_amount = request.POST.get('input3.1')
            model2.food_price = request.POST.get('input3.2')
            model2.date_time = datetime.now()
            model2.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input3.0'))
            random.append_food_amount(request.POST.get('input3.1'))
            random.append_food_price(request.POST.get('input3.2'))
            random.append_order_time(datetime.now())
           

         # select the table of the user who is logged in 
        # if the user post and change in the fourth vegan food type
        # it save the data in the module
        if request.POST.get('input4.0'):
            model3 = FoodVegan.objects.select_related("owner").filter(owner=o).get(id=4)
            model3.owner  = request.user                
            model3.food_name = request.POST.get('input4.0')
            model3.food_amount = request.POST.get('input4.1')
            model3.food_price = request.POST.get('input4.2')
            model3.date_time = datetime.now()
            model3.save()

            # append the saved data in the instance of the class 
            random.append_food_name(request.POST.get('input4.0'))
            random.append_food_amount(request.POST.get('input4.1'))
            random.append_food_price(request.POST.get('input4.2'))
            random.append_order_time(datetime.now())
              
        
        random.set_food_type("Vegan") 
        print(random)    

        return redirect('finallist')

    # mutators to append the list in the __init__ method
    def append_food_name(self, name):
        self.food_name.append(name)
        

    def append_food_amount(self, amount):
        self.food_amount.append(amount)
        
    
    def append_food_price(self, price):
        self.food_price.append(price)
        
    
    def append_order_time(self, time_o):
        self.food_order_time.append(time_o)

    # mutators of method __init__
    def set_food_name(self, name):
        self.food_name = name
        

    def set_food_amount(self, amount):
        self.food_amount = amount
            
        
    def set_food_price(self, price):
        self.food_price = price
            
        
    def set_order_time(self, time_o):
        self.food_order_time = time_o  

    # getters of method __init__
    def get_food_name(self):
        for i in self.food_name:
            print(i)

    def get_food_amount(self):
        for i in self.food_amount:
            print(i)

    def get_food_price(self):
        for i in self.food_price:
            print(i)

    def get_order_time(self):
        for i in self.food_order_time:
            print(i)

    #prints the state of the class
    def __str__(self):
        return "\n\nDetails of the order are...\nUser name: " + str(self.username)+ "\nUser id: " + str(self.id) + "\nFood category: " + str(self.get_food_type())  + "\nFood name: " + str(self.food_name) + "\nFood amount: " + str(self.food_amount) + "\nFood price: " + str(self.food_price) + "\nFood Order time: " + str(self.food_order_time) + "\n"

    
 # class to display final recipe
class Receipt(ListView):

    # address of the final list template
    template_name="userinterface/FinalList.html"   

    # method to store the state of the class
    def __init__(self):
        self.username = ""
        self.id = ""
        self.all_orders = []
        self.total_price = "" 
    
    # get method display the recipe template on get request 
    def get(self,request): 

        # for OOP programming
        # creating the instance of the class recipe
        random = Receipt()

        # setting username and id in the instance of the class
        random.set_username(request.user.username)
        random.set_id(request.user.id)

        # getting the data from the database according to the logged in user
        # only order that was made at latest 15 minutes ago is called
        o = request.user.id
        context = {}

        # all the three models containg different types of food Veg, Nonveg and Vegan         
        item = Food.objects.select_related('owner').filter(Q(owner=o)&Q(date_time__gte=(datetime.now()-timedelta(minutes=15)),date_time__lte=datetime.now())).values()
        item1 = FoodNon.objects.select_related('owner').filter(Q(owner=o)&Q(date_time__gte=(datetime.now()-timedelta(minutes=15)),date_time__lte=datetime.now())).values()
        item2 = FoodVegan.objects.select_related('owner').filter(Q(owner=o)&Q(date_time__gte=(datetime.now()-timedelta(minutes=15)),date_time__lte=datetime.now())).values()
        
        # store the total value of the order
        total_sum = 0

        # if no data is found in the database pass
        # else make an array to store the value and pass to html for displaying 
        # and append the data in instance of the class for oop displaying
        if not item:
            pass            
        else:
            value = []
            # loopes over all the item from database
            # read the price of product and added it to total sum
            # makes an array of the orders from the database and append them in an array
            for i in item:

                total_sum += i['food_price']                                                
                values ={key:i[key] for key in ['food_name','food_amount','food_price','date_time']}
                value.append(values)

                random.append_order(values)
            # passing the values to the html                
            context['list'] = value

        # Same is done for second model or nonvegetarian orders
        if not item1:
            pass            
        else:
            value1 = []
            for i in item1: 
                total_sum += i['food_price']                                
                values1 ={key:i[key] for key in ['food_name','food_amount','food_price','date_time']}
                value1.append(values1)

                random.append_order(values1)
                
            context['list1'] = value1

        # Same is done for vegan model
        if not item2:
            pass            
        else:
            value2 = []
            for i in item2:
                total_sum += i['food_price']                                 
                values2 ={key:i[key] for key in ['food_name','food_amount','food_price','date_time']}
                value2.append(values2) 

                random.append_order(values2)              
            context['list2'] = value2

           

        context['sum'] = total_sum    

        # print the instance of the class
        print(random)     
        
        return render(request, self.template_name,context)

    # accessors and mutators methods
    def post(self,request):
        return render(request, self.template_name, {})


    def append_order(self, order):
        self.all_orders.append(order)

    
    def get_orders(self):
        return self.all_orders

    def set_username(self, username):
        self.username = username

    def get_username(self):
        self.username

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    # method to print the state of the function
    def __str__(self):
        return "\n\n All Orders\n\n Username: " + str(self.username) + "\n User Id: " + str(self.id) + "\n User Order details: " + str(self.all_orders)

 

######################## End ######################################