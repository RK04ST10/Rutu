from django.contrib import admin
from webapp.models import *

# Register your models here.


class BookTableAdmin(admin.ModelAdmin):
    list_display = ['Name', 'People', 'Task']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Msg']


admin.site.register(BookTable, BookTableAdmin)
admin.site.register(Contact, ContactAdmin)