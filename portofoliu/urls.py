from django.urls import path
from .views import portofoliu_home
from .views import portofoliu_view, portofoliu_picturi, portofoliu_portrete, portofoliu_creion, portofoliu_ilustratii, portofoliu_nft

urlpatterns = [
    path('', portofoliu_home, name='portofoliu_home'),
    path('portofoliu/', portofoliu_view, name='portofoliu_meniu'),
    path('portofoliu/picturi', portofoliu_picturi, name='portofoliu_picturi'),
    path('portofoliu/portete', portofoliu_portrete, name='portofoliu_portrete'),
    path('portofoliu/creion', portofoliu_creion, name='portofoliu_creion'),
    path('portofoliu/ilustratii', portofoliu_ilustratii, name='portofoliu_ilustratii'),
    path('portofoliu/nft', portofoliu_nft, name='portofoliu_nft'),
]