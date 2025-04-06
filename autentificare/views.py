from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def autentificare_si_inregistrare_view(request):
    inregistrare = request.GET.get('inregistrare')  # Verificăm dacă parametrul 'inregistrare' este prezent
    if request.method == 'POST':
        if 'inregistrare' in request.POST:
            form_inregistrare = UserCreationForm(request.POST, prefix='inregistrare')
            form_autentificare = AuthenticationForm(prefix='autentificare')
            if form_inregistrare.is_valid():
                form_inregistrare.save()
                messages.success(request, "Contul dvs. a fost creat cu succes! Vă rugăm să vă autentificați.")
                return redirect('autentificare')
        elif 'autentificare' in request.POST:
            form_autentificare = AuthenticationForm(data=request.POST, prefix='autentificare')
            form_inregistrare = UserCreationForm(prefix='inregistrare')
            if form_autentificare.is_valid():
                user = form_autentificare.get_user()
                login(request, user)
                messages.success(request, "Autentificare reușită!")
                return redirect('home')
    else:
        form_inregistrare = UserCreationForm(prefix='inregistrare')
        form_autentificare = AuthenticationForm(prefix='autentificare')

    # Afișăm formularul de înregistrare dacă parametrul 'inregistrare' este prezent
    if inregistrare:
        return render(request, 'autentificare/autentificare_si_inregistrare.html', {
            'form_inregistrare': form_inregistrare,
            'form_autentificare': None
        })

    return render(request, 'autentificare/autentificare_si_inregistrare.html', {
        'form_inregistrare': form_inregistrare,
        'form_autentificare': form_autentificare
    })

def delogare_view(request):
    logout(request)
    messages.success(request, "Te-ai delogat cu succes!")
    return redirect('home')