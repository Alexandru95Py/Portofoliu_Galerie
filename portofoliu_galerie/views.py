from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from galerie.models import Tablou
from portofoliu.models import Proiect

def home(request):
    return render(request, "portofoliu_galerie/home.html")

def contact(request):
    if request.method == "POST":
        nume = request.POST.get("nume")
        email = request.POST.get("email")
        mesaj = request.POST.get("mesaj")

        send_mail(
            subject=f"Mesaj de la {nume}",
            message=f"Email: {email}\n\nMesaj:\n{mesaj}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['alexandru.goga18@gmail.com'],
            fail_silently=False,
        )

        print("Nume", nume)
        print("Email", email)
        print("Mesaj", mesaj)

        return render(request, "portofoliu_galerie/contact.html" , {"success":True})
    return render(request, "portofoliu_galerie/contact.html")

def despre(request):
    return render(request, "portofoliu_galerie/despre.html")

@api_view(['GET'])
def api_home_data(request):
    tablouri = list(Tablou.objects.all().values('id', 'titlu', 'imagine')[:3])
    proiecte = list(Proiect.objects.all().values('id', 'titlu', 'link')[:3])
    mesaj = "Bine ai venit pe platforma"