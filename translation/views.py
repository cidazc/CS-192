from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SearchForm
from .forms import TranslationForm
from .forms import TranslationOriginTextForm
from .models import Search
from .models import Translation
from .models import Translation_origin_text
from django.db.models import Q
from .forms import UpvoteForm
from .forms import DownvoteForm

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

def delete_translation(request):
    print("It is here")
    form = TranslationOriginTextForm(request.POST)
    try:
        if request.method == "POST":
            if form.is_valid:
                print("It is here 2")
                print(request.POST.copy())
                data = request.POST.copy()
                delete = data.get('origin_text')
                print(delete)
                to_delete = Translation.objects.filter(origin_text = delete)
                to_delete.delete()
                return render(request,'translation/translation_deleted.html')
    except:
        messages.error(request,form.errors)
        print("Translation does not exist")
        return render(request,'translation/translation_does_not_exist.html')

    context = {'form': form}
    return render(request,'translation/delete_translation.html', context)

def upvote(request):
    print("It is here")
    form = UpvoteForm(request.POST)
    try:
        if request.method == "POST":
            if form.is_valid:
                print(request.POST.copy())
                data = request.POST.copy()
                text = data.get('origin_text')
                print(text)
                u = Translation.objects.get(origin_text = text)
                u.upvotes = u.upvotes + 1
                u.save()
                return render(request,'translation/translation.html')


    except:
        messages.error(request,form.errors)
        print("Translation does not exist")
        return render(request,'translation/translation_dne.html')

    context = {'form': form}
    return render(request,'translation/user_upvote.html', context)

def downvote(request):
    print("It is here")
    form = DownvoteForm(request.POST, instance = request.user)
    try:
        if request.method == "POST":
            if form.is_valid:
                print(request.POST.copy())
                data = request.POST.copy()
                text = data.get('origin_text')
                print(text)
                u = Translation.objects.get(origin_text = text)
                u.downvotes = u.downvotes + 1
                u.save()
                return render(request,'translation/translation_list.html')


    except:
        messages.error(request,form.errors)
        print("Translation does not exist")
        return render(request,'translation/translation_dne.html')

    context = {'form': form}
    return render(request,'translation/user_downvote.html', context)

def search(request, id=id):
    search = Search.objects.get(id=id)
    return render(request, 'translation/search.html', {'search': search})

def translation(request, id=id):
    translation = Translation.objects.get(id=id)
    return render(request, 'translation/translation.html', {'translation': translation})
