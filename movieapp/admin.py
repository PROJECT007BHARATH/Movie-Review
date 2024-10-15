from django.contrib import admin
from .models import movie
from .models import Review

# Register your models here.
admin.site.register(movie)
admin.site.register(Review)