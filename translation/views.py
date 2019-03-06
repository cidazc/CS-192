from django.shortcuts import render, get_object_or_404
from .forms import BlogForm
from .forms import TranslationForm
from .models import Blog
from .models import Translation
# Create your views here.
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
    else:
        form = BlogForm()
    return render(request, 'translation/blog_form.html', {'form':form})

def add_translation(request):
    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
    else:
        form = TranslationForm()
    return render(request, 'translation/translation_form.html', {'form':form})

def edit_blog(request, id=None):
    item = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    return render(request, 'translation/blog_form.html', {'form':form})

def edit_translation(request, id=None):
    item = get_object_or_404(Translation, id=id)
    form = TranslationForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    return render(request, 'translation/translation_form.html', {'form':form})
