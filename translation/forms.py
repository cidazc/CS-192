from django.forms import ModelForm
from .models import Blog
from .models import Translation

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','description']

class TranslationForm(ModelForm):
    class Meta:
        model = Translation
        fields = '__all__'
