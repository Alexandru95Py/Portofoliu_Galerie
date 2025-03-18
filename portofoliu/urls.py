from django.urls import path
from .views import portofoliu_home

urlpatterns = [
    path('', portofoliu_home, name='portofoliu_home'),
]