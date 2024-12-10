from django.contrib import admin
from . models import Articles
# Register your models here.
@admin.register(Articles)
class AdminArticles(admin.ModelAdmin):
    list_display = ['name','description']
    # list_display_links = ['name']