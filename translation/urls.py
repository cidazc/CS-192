from django.conf.urls import url
from django.urls import path
from . import views
from .views import(
    TranslationListView
)

urlpatterns = [
    url(r'^search/add/$', views.add_search, name='add_search'),
    url(r'^translation/add/$', views.add_translation, name='add_translation'),
    url(r'^search/edit/(?P<id>\d+)/$', views.edit_search, name='edit_search'),
    url(r'^translation/edit/(?P<id>\d+)/$', views.edit_translation, name='edit_translation'),
    url(r'^translation/(?P<id>\d+)/$', views.translation, name='translation'),
    url(r'^search/(?P<id>\d+)/$', views.search, name='search'),
    path('translation/', TranslationListView.as_view(), name = 'translation-list'),
]
