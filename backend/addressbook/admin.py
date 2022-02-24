from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')

admin.site.register(Contact, ContactAdmin)