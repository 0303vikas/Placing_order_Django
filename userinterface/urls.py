from django.urls import path, include
from userinterface import views
from django.contrib.auth.decorators import login_required


# all the routes  to all the pages
urlpatterns = [
    path("login/", views.LoginPage.as_view(), name="login"),
    path("register/",views.Register.as_view(), name="register"),
    path("logout/", views.Logoutpage.as_view(), name="logout"),
    path("user/foodtype/", login_required(views.Home.as_view(),login_url='login'), name="home"),    
    path("user/VegFood/", login_required(views.VegetarianFood.as_view()), name="vegfood"),
    path("user/NonVegFood/", login_required(views.NonVegFood.as_view()), name="nonvegfood"),
    path("user/VeganFood/", login_required(views.VeganFood.as_view()), name="veganfood"),
    path("user/Order/", login_required(views.Receipt.as_view()),name='finallist'),

]