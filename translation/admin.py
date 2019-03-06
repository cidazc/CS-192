from django.contrib import admin

# Register your models here.

from .models import Translation
from .models import Blog #

admin.site.register(Translation)
admin.site.register(Blog)
