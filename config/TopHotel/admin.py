from django.contrib import admin
from .models import *

# Register your models here.
class HuespedAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','dni','telefono']
    list_display_links = ['nombre','apellido','dni','telefono']
    fieldsets = (
        ('Datos',{
            'fields': ('nombre','apellido','dni','telefono')
        }),
    )

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['numero','piso']
    list_display_links = ['numero','piso']
    fieldsets = (
        ('Datos',{
            'fields': ('numero','piso')
        }),
    )

admin.site.register(Huesped, HuespedAdmin)
admin.site.register(Habitacion, HabitacionAdmin)