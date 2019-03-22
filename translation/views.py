from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from .forms import TranslationForm
from .models import Search
from .models import Translation
from django.db.models import Q

from django_filters.views import FilterView
from .filters import TranslationFilter
from django.contrib.auth.models import User


from django.views.generic import (
CreateView,
DetailView,
ListView,
UpdateView,
DeleteView
)
# Create your views here.

class TranslationListView(ListView):
    template_name = 'translation/translation_list.html'
    queryset = Translation.objects.all()

class TranslationSearch(FilterView):
    model = Translation
    filterset_class = TranslationFilter
    context_object_name = 'origin_text'
    paginate_by = 50
    template_name = 'translation/search_list.html'

def add_translation(request):
    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            translation_item = form.save(commit=False)
            translation_item.save()
            return redirect('/translation/'+str(translation_item.id)+'/')
    else:
        form = TranslationForm()
    return render(request, 'translation/translation_form.html', {'form':form})

def edit_translation(request, id=None):
    item = get_object_or_404(Translation, id=id)
    form = TranslationForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/translation/'+str(item.id)+'/')
    return render(request, 'translation/translation_form.html', {'form':form})

def search(request, id=id):
    search = Search.objects.get(id=id)
    return render(request, 'translation/search.html', {'search': search})

def translation(request, id=id):
    translation = Translation.objects.get(id=id)
    return render(request, 'translation/translation.html', {'translation': translation})
