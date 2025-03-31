from django.shortcuts import render, get_object_or_404, redirect
from .models import Tablou, Comentariu, Like
from django.utils.timezone import now
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

def galerie_home(request):
    tablouri = Tablou.objects.all()
    # Debugging: Afișăm datele în consolă pentru verificare
    print("Debug: Tablouri transmise către șablon:")
    for tablou in tablouri:
        print(f"ID: {tablou.id}, Likes: {tablou.likes}")
    return render(request, "galerie/galerie.html", {"tablouri": tablouri})

@login_required
def adauga_like(request, tablou_id):
    tablou = get_object_or_404(Tablou, id=tablou_id)

    if request.method == "POST":
        user = request.user
        liked = Like.objects.filter(user=user, tablou=tablou).exists()

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
def api_tablouri(request):
    tablouri = Tablou.objects.all().values('id', 'titlu', 'descriere', 'imagine')
    return Response(tablouri)

# Create your views here.
