from django.shortcuts import render
#from .models import Memory

def register_user(request):
    return render(request, 'users/register.html')
