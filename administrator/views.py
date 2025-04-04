from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def admin_home(request):
    return HttpResponse("<h1>Administrator</h1><p>Aici vor fi setarile pentru administrare</p>")

# Create your views here.
