from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Emissions

# Register your models here.
class EmissionsAdmin(admin.ModelAdmin):
    list_display =  ['id', 'date_created', 'accounting_period', 'scope_1', 'scope_2','scope_3']
    ordering = ['date_created']
 
admin.site.register(Emissions, EmissionsAdmin)
