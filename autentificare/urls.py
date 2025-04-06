from django.urls import path
from .views import autentificare_si_inregistrare_view, delogare_view

urlpatterns = [
    path('autentificare/', autentificare_si_inregistrare_view, name='autentificare'),
    path('delogare/', delogare_view, name='delogare'),
]
