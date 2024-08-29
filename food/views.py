from django.shortcuts import render

# Create your views here.
def fooditems(request):
    return render(request, 'fooditems.html')
