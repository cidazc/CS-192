from django.forms import ModelForm, TextInput, Textarea
from .models import Search
from .models import Translation
from django.contrib.auth.models import User

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

class TranslationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(TranslationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Translation
        fields = '__all__'
        widgets = {
            'origin_text': Textarea(attrs={'class': 'form-control'}),
            'target_text': Textarea(attrs={'class': 'form-control'}),
            'origin_language': TextInput(attrs={'class': 'form-control'}),
            'target_language': TextInput(attrs={'class': 'form-control'}),
            'context_examples': Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'origin_text':'Origin text',
            'target_text':'Target text',
            'origin_language':'Origin language',
            'target_language':'Target language',
            'context_examples':'Usage',
        }


class MakeUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
