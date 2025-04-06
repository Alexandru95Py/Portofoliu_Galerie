"""
URL configuration for portofoliu_galerie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, contact, despre
from django.conf import settings
from django.conf.urls.static import static
from administrator.views import admin_home
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin este deja configurat aici
    path('galerie/', include('galerie.urls')),
    path('', home, name='home'),
    path('portofoliu/', include('portofoliu.urls')),
    path('administrator/', admin_home, name='admin_home'),  # Restaurăm ruta pentru admin_home
    path('contact/', contact, name='contact'),
    path('despre/', despre, name='despre'),
    path('api/', include('galerie.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Redirecționare de la /about la /despre
    path('cont/', include('autentificare.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)