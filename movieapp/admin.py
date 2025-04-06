from django.contrib import admin
from .models import *

# Register your models here.
class MyMovie(admin.ModelAdmin):
  list_display = ('name', 'description', 'trailer', 'year', 'star', 'show')
  list_filter = ('star', 'show')

admin.site.register(Movie, MyMovie)

