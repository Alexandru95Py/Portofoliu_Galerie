from django.shortcuts import render
from rest_framework.response import Response
from .models import Proiect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_proiecte(request):
    proiecte = Proiect.objects.all().values('id', 'titlu', 'categorie', 'descriere', 'link', 'imagine' )
    return Response(proiecte)


def portofoliu_home(request):
    proiecte = Proiect.objects.all()
    return render(request, 'portofoliu/portofoliu.html', {'proiecte': proiecte})

def portofoliu_view(request):
    return render(request, 'portofoliu/portofoliu.html')

def portofoliu_picturi(request):
    proiecte = Proiect.objects.filter(categorie='ulei')  # Corectăm categoria
    return render(request, 'portofoliu/picturi.html', {'proiecte': proiecte})

def portofoliu_portrete(request):
    proiecte = Proiect.objects.filter(categorie='portret')
    return render(request, 'portofoliu/portrete.html', {'proiecte': proiecte})

def portofoliu_creion(request):
    proiecte = Proiect.objects.filter(categorie='creion')
    return render(request, 'portofoliu/creion.html', {'proiecte': proiecte})

def portofoliu_ilustratii(request):
    proiecte = Proiect.objects.filter(categorie='ilustratie')
    return render(request, 'portofoliu/ilustratii.html', {'proiecte': proiecte})

def portofoliu_nft(request):
    proiecte = Proiect.objects.filter(categorie='nft')
    return render(request, 'portofoliu/nft.html', {'proiecte': proiecte})
