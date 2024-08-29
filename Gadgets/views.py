from django.shortcuts import render

# Create your views here.
def gadgetsitems(request):
    return render(request, 'gadgetsitems.html')