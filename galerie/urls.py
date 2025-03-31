from django.urls import path
from .views import galerie_home, adauga_like, adauga_comentariu
from galerie.views import api_tablouri

# Rutele pentru aplicația GALERIE:
# - Afișare pagină principală
# - Adăugare/ștergere like
# - Adăugare comentariu
# - Endpoint API REST pentru tablouri


urlpatterns = [
    path('', galerie_home, name='galerie_home'),
    path('like/<int:tablou_id>/', adauga_like, name='adauga_like'),
    path('comentariu/<int:tablou_id>/', adauga_comentariu, name='adauga_comentariu'),
    path('tablouri/', api_tablouri, name='api_tablouri'),
]