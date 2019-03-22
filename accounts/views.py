from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, UsernameForm
from django.contrib.auth.models import User
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
#
def user_deleted(request):
    return render(request, 'user_deleted.html')

def remove_user(request):
    print("It is here")
    form = UsernameForm(request.POST, instance = request.user)
    try:
        if request.method == "POST":
            if form.is_valid:
                print("It is here 2")
                print(request.POST.copy())
                data = request.POST.copy()
                delete = data.get('username')
                print(delete)
                u = User.objects.get(username = delete)
                u.delete()
                return render(request,'user_deleted.html')


    except:
        messages.error(request,form.errors)
        print("Username does not exist")
        return render(request,'user_does_not_exist.html')

    context = {'form': form}
    return render(request,'remove_user.html', context)
