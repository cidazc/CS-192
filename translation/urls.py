from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/blog/$', views.add_blog, name='add_blog'),
    url(r'^add/translation/$', views.add_translation, name='add_translation'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^edit/translation/(?P<id>\d+)/$', views.edit_translation, name='edit_translation'),
    url(r'^translation/(?P<id>\d+)/$', views.translation, name='translation'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),

]
