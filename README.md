# Placing_order_Django
A food ordering Website, made with Django with OOP principle of python programming.

## Setup

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver 5000
```
And navigate to `http://127.0.0.1:5000/login/`.

In order to test the purchase flows, fill in the account details in
`project/gc_app/views.py` to match your **SANDBOX** developer credentials.

## Walkthrough Routes
Follow the 'Food ordering Web Application (1).pdf' 

###Routes
>login/ [name='login']
>register/ [name='register']
>logout/ [name='logout']
>user/foodtype/ [name='home']
>user/VegFood/ [name='vegfood']
>user/NonVegFood/ [name='nonvegfood']
>user/VeganFood/ [name='veganfood']
>user/Order/ [name='finallist']
>admin/
>login/ [name='login']
>logout/ [name='logout']
>password_change/ [name='password_change']
>password_change/done/ [name='password_change_done']
>password_reset/ [name='password_reset']
>password_reset/done/ [name='password_reset_done']
>reset/<uidb64>/<token>/ [name='password_reset_confirm']
>reset/done/ [name='password_reset_complete']
>^static/(?P<path>.*)$



