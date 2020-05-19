from django.contrib import admin
from . import models

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year','title','length']

    search_fields = ['title','length']

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
