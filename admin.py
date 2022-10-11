from django.contrib import admin

# Register your models here.
from recipe.models import *

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Suggestion)