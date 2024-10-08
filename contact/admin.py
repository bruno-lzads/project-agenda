from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'email', 'created_date', 'category', 'show',
    ordering = '-id', #Ordena a lista
    search_fields = 'id', 'first_name', 'email',
    list_per_page = 10
    list_max_show_all = 15 #Lime de campos ao mostrar tudo
    list_editable = 'show', #first_name', 'last_name' #edita o input
    list_display_links = 'id', 'first_name'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', #Ordena a lista