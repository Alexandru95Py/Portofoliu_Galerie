from django.shortcuts import render
from django.http import HttpResponse

def portofoliu_home(request):
    return render(request, 'portofoliu/portofoliu.html')

def portofoliu_view(request):
    return render(request, 'portofoliu/portofoliu.html')

def portofoliu_picturi(request):
    return render(request, 'portofoliu/picturi.html')

def portofoliu_portrete(request):
    return render(request, 'portofoliu/portrete.html')

def portofoliu_creion(request):
    return render(request, 'portofoliu/creion.html')

def portofoliu_ilustratii(request):
    return render(request, 'portofoliu/ilustratii.html')

def portofoliu_nft(request):
    return render(request, 'portofoliu/nft.html')



# Create your views here.
