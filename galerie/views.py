from django.shortcuts import render, get_object_or_404, redirect
from .models import Tablou, Comentariu, Like
from django.utils.timezone import now
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.urls import reverse

from rest_framework.response import Response
from django.views.decorators.http import require_POST

def galerie_home(request):
    tablouri = Tablou.objects.all()
    # Debugging: Afișăm datele în consolă pentru verificare
    print("Debug: Tablouri transmise către șablon:")
    for tablou in tablouri:
        print(f"ID: {tablou.id}, Likes: {tablou.likes}")
    return render(request, "galerie/galerie.html", {"tablouri": tablouri})

@login_required(login_url=settings.LOGIN_URL)  # Specificăm explicit LOGIN_URL
@require_POST
@csrf_exempt
def adauga_like(request, tablou_id):
    tablou = get_object_or_404(Tablou, id=tablou_id)
   
    if request.method == "POST":
        user = request.user
        liked = Like.objects.filter(user=user, tablou=tablou).exists()
        print(f"User: {user}, Tablou ID: {tablou_id}, Liked: {liked}")

        if liked:
            Like.objects.filter(user=user, tablou=tablou).delete()
            tablou.likes -= 1
            liked = False
        else:
            Like.objects.create(user=user, tablou=tablou)
            tablou.likes += 1
            liked = True

        tablou.save()
        return JsonResponse({"liked": liked, "like_count": tablou.likes})

    return JsonResponse({"success": False, "error": "Doar metode POST acceptate"}, status=400)

@csrf_exempt
def adauga_comentariu(request, tablou_id):
    if not request.user.is_authenticated:
        autentificare_url = "http://127.0.0.1:8000/cont/autentificare/"  # Link corect către autentificare
        inregistrare_url = "http://127.0.0.1:8000/cont/autentificare/?inregistrare=1"  # Link pentru înregistrare
        mesaj = (
            f"Trebuie să fii autentificat pentru a comenta. "
            f"<a href='{autentificare_url}'>Autentificare</a> sau "
            f"<a href='{inregistrare_url}'>Înregistrare</a>."
        )
        return JsonResponse({"success": False, "error": mesaj}, status=403)

    if request.method == "POST":
        tablou = get_object_or_404(Tablou, id=tablou_id)
        nume = request.POST.get("name", "")
        text = request.POST.get("text", "")

        if not nume or not text:
            return JsonResponse({"success": False, "error": "Toate câmpurile sunt obligatorii"}, status=400)

        comentariu = Comentariu.objects.create(tablou=tablou, nume=nume, text=text)

        return JsonResponse({"success": True, "name": comentariu.nume, "text": comentariu.text})

    return JsonResponse({"error": "Metodă invalidă"}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_tablouri(request):
    tablouri = Tablou.objects.all().values('id', 'titlu', 'descriere', 'imagine')
    return Response(tablouri)

# Create your views here.
