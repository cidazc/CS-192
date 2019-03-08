from django.forms import ModelForm
from .models import Search
from .models import Translation

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields = '__all__'
