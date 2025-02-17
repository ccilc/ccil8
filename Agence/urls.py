from django.urls import path, include
from . import views
from .views import *

urlpatterns = [

    path('', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('propos', propos, name='propos'),
    path('galerie', galerie, name='galerie'),
    path('contactez', contactez, name='contactez'),
    path('visite', visite, name='visite'),
    path('signup', signup_view, name='signup'),
    path('connexion', connexion, name='connexion'),
    path('inscription', inscription, name='inscription'),


    path('chambre_list', views.chambre_list, name='chambre_list'),
    path('reserver/<int:chambre_id>/', views.reserver_chambre, name='reserver_chambre'),
    path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),

]
