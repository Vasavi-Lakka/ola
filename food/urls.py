from django.urls import path
from food.views import *

app_name='ITEMS'

urlpatterns=[
    path('fooditems/', fooditems, name='fooditems'),  # type: ignore
]