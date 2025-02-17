from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from Agence.form import CustomUserCreationForm


# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


def login(request, *args, **kwargs):
    return render(request, 'login.html', {})


def register(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigez l'utilisateur vers la page d'accueil ou une autre page
        else:
            messages.error(request, 'Identifiants incorrects.')
    return render(request, 'register.html', {})


def propos(request, *args, **kwargs):
    return render(request, 'propos.html', {})


def galerie(request, *args, **kwargs):
    return render(request, 'galerie.html', {})


def contactez(request, *args, **kwargs):
    return render(request, 'contactez.html', {})


def visite(request, *args, **kwargs):
    return render(request, 'visite.html', {})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse email est déjà utilisée.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')  # Redirigez l'utilisateur après la création du compte

    return render(request, 'signup.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chambre_list')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'register.html')


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login.html', {'form': form})







# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chambre, Reservation
from .forms import ReservationForm


def chambre_list(request):
    chambres = Chambre.objects.all()  # Récupère toutes les chambres
    reservations = Reservation.objects.all()  # Récupère toutes les réservations
    return render(request, 'addandshow.html', {'chambres': chambres, 'reservations': reservations})


def reserver_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambre, id=chambre_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.chambre = chambre  # Lier la chambre sélectionnée à la réservation
            reservation.save()
            return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = ReservationForm()

    return render(request, 'reserver_chambre.html', {'form': form, 'chambre': chambre})


def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})
