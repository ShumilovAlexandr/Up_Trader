from django.contrib import admin

from .models import (Title,
                     SubTitle)


@admin.register(Title)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ['name']}

@admin.register(SubTitle)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    prepopulated_fields = {'slug': ['name']}
