from django.contrib import admin
from .models import Category,Teacher

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'rate','available']
    list_filter = ['available']
    list_editable = ['rate']
    prepopulated_fields = {'slug': ('name',)}
