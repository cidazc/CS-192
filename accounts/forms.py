from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Username

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UsernameForm(ModelForm):
    class Meta:
        model = Username
        fields = '__all__'
