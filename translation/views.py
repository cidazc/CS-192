from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from .forms import TranslationForm
from .models import Search
from .models import Translation
from django.db.models import Q

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


def add_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_item = form.save(commit=False)
            search_item.save()
            return redirect('/search/'+str(search_item.id)+'/')
    else:
        form = SearchForm()
    return render(request, 'translation/search_form.html', {'form':form})

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

def edit_search(request, id=None):
    item = get_object_or_404(Search, id=id)
    form = SearchForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/search/'+str(item.id)+'/')
    return render(request, 'translation/search_form.html', {'form':form})

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
