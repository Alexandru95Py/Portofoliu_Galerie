from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

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
        return render(request, "portofoliu_galerie/contact.html" , {"success":True})
    return render(request, "portofoliu_galerie/contact.html")

def despre(request):
    return render(request, "portofoliu_galerie/despre.html")
