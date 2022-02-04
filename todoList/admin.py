from django.contrib import admin
from todoList.models import todoList

class todoListAdmin(admin.ModelAdmin):
    list_display = ('item_name',)

admin.site.register(todoList,todoListAdmin)