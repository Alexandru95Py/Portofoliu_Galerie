from django.contrib import admin
from .models import Proiect


from django.contrib import admin
from .models import Proiect

@admin.register(Proiect)
class ProiectAdmin(admin.ModelAdmin):
    list_display = ['titlu', 'categorie']
    list_filter = ['categorie']
    search_fields = ['titlu', 'categorie']

    @admin.action(description="Schimba categoria in 'Portrete'")
    def schimba_categorie(self, request, queryset):
        queryset.update(categorie='Portrete')


# Register your models here.
