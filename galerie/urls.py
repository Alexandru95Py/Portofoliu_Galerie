from django.urls import path
from .views import galerie_home, adauga_like, adauga_comentariu

urlpatterns = [
    path('', galerie_home, name='galerie_home'),
    path('like/<int:tablou_id>/', adauga_like, name='adauga_like'),
    path('comentariu/<int:tablou_id>/', adauga_comentariu, name='adauga_comentariu')
]