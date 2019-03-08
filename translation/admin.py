from django.contrib import admin

# Register your models here.

from .models import Translation
from .models import Search #

admin.site.register(Translation)
admin.site.register(Search)
