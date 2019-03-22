from django.contrib.auth.forms import UserCreationForm
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
# def remove_user(request):
#     if request.method == 'POST':
#         form = RemoveUser(request.POST)
#
#         if form.is_valid():
#             rem = User.objects.get(username=form.cleaned_data['username'])
#             if rem is not None:
#                 rem.delete()
#                 return redirect('main')
#             else:
#                ## Send some error messgae
#                 print("There is an error")
#     else:
#         form = RemoveUser()
#     context = {'form': form}
#     return render(request, 'remove_user.html', context)

def remove_user(request):
    print("It is here")
    form = UsernameForm(request.POST, instance = request.user)
    if form.is_valid:
        print(request.POST.copy())
        data = request.POST.copy()
        delete = data.get('username')
        print(delete)
        u = User.objects.get(username = delete)
        u.delete()

    else:
        messages.error(request,form.errors)
    context = {'form': form}
    return render(request,'remove_user.html', context)
