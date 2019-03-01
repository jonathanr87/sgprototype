from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def map(request):

    return render(request,'map/map.html')

