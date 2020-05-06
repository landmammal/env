from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from .forms import UserForm


from .models import User


# Create your views here.
def home(request, user_id):

    # try:
    #     context = {'user': User.objects.get(pk=user_id)}
    # except User.DoesNotExist:
    #     raise Http404("user not found")

    user = get_object_or_404(User, pk=user_id)

    context = {'user': User.objects.get(pk=user_id)}



  
    return render(request, 'users/home.html', context)

# Create a class for your model that subclasses
#   the generic view you want. This serves as an
#   index view.
class UserListView(ListView):
    # Finally, tell the generic view what model
    #   it applies to, and which template to use.
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        # In real life we'd retrieve this from the session.
        context['power_level'] = 'Godly'
        
        return context


    model = User
    template_name = 'users/index.html'

def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            User(
                name= form.cleaned_data['name'],
                nickname= form.cleaned_data['nickname'],                
                age= form.cleaned_data['age']
            ).save()

            return redirect('users:index')
        else:
            return render(request,'user/add.html', {'form': form})
    
    else:
        context = {'header' : 'GET', 'form': UserForm() }

        return render(request, 'users/add.html', context)



