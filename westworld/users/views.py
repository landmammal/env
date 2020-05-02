from django.shortcuts import render
from django.http import HttpResponse

from .models import User


# Create your views here.
def home(request):
    # response = """
    #     <h1> Good Python </h1>
    # """
    # return HttpResponse(response)
    context = {
        'name': 'Aries',
        'users': User.objects.all(),
    }
    return render(request, 'users/home.html', context)

    

