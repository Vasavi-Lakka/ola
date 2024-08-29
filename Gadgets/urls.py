from django.urls import path
from Gadgets.views import * # type: ignore
 
app_name='EleItems'

urlpatterns=[
    path('gadgetsitems/', gadgetsitems, name='gadgetsitems'),
    
]
