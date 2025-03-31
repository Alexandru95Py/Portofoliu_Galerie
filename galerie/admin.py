from django.contrib import admin
from .models import Tablou, Comentariu

# Admin personalizat pentru modelul Tablou
class TablouAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'descriere', 'likes')
    search_fields = ('titlu', 'descriere')
    list_filter = ('likes',)

# Admin personalizat pentru modelul Comentariu
class ComentariuAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tablou', 'data')
    search_fields = ('nume', 'text')
    list_filter = ('data',)

# Înregistrare modele în admin cu clasele de mai sus
admin.site.register(Tablou, TablouAdmin)
admin.site.register(Comentariu, ComentariuAdmin)
