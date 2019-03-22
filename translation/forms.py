from django.forms import ModelForm
from .models import Search
from .models import Translation
from django.contrib.auth.models import User

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields = '__all__'

class MakeUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
