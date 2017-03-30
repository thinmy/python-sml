from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'active')
    list_display = ('name', 'active')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
