import django_filters
from .models import Translation

class TranslationFilter(django_filters.FilterSet):
    class Meta:
        model = Translation
        fields = ['origin_text']
