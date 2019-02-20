
"""

Allan Matthew B. Mariano 
2015-05804


“This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof.
 Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, 
 Diliman for the AY 2018-2019”.

"""










"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# my_project/urls.py
from django.contrib import admin
from . import views
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path('delete', views.delete),
    path('add', views.add),
    path('delete2', views.delete2),
    path('add2', views.add2),
    path('moderator', views.moderator)
]
