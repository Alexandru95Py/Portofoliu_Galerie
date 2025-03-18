from django.shortcuts import render
from django.http import HttpResponse

def portofoliu_home(request):
    return render(request, 'portofoliu/portofoliu.html')

# Create your views here.
