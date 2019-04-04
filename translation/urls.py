from django.conf.urls import url
from django.urls import path
from . import views
from .views import(
    TranslationListView,
    TranslationSearch
)

urlpatterns = [
    url(r'^translation/add/$', views.add_translation, name='add_translation'),
    url(r'^translation/edit/(?P<id>\d+)/$', views.edit_translation, name='edit_translation'),
    url(r'^translation/(?P<id>\d+)/$', views.translation, name='translation'),
    path('translation/', TranslationListView.as_view(), name = 'translation-list'),
    path('translation_search/', TranslationSearch.as_view(), name = 'translation-search'),
    path('translation/remove/', views.delete_translation, name = 'delete-translation'),

]
