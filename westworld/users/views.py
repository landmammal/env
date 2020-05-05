from django.shortcuts import render
from django.http import HttpResponse

from .models import User


# Create your views here.
def home(request, user_id):
    context = {
        'user': User.objects.get(pk=user_id)
    }
    return render(request, 'users/home.html', context)
    

    

