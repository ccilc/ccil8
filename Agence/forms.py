from django import forms
from django.forms import fields
#from .models import User


#class StudentRegistration(forms.ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['id','name', 'email', 'password']

    #    widgets = {
     #       'name': forms.TimeInput(attrs={'class': 'form-control'}),
      #      'email': forms.EmailInput(attrs={'class': 'form-control'}),
       #     'password': forms.PasswordInput( render_value=True, attrs={'class': 'form-control'})  #render_value = true pour que le mot de passe s'affiche dans Modifier
        #}


# forms.py
# forms.py
from django import forms
from .models import Reservation, Chambre
from django.forms.widgets import SelectDateWidget

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_client', 'email_client', 'date_debut', 'date_fin']
        widgets = {
            'date_debut': SelectDateWidget(years=range(2025, 2031)),
            'date_fin': SelectDateWidget(years=range(2025, 2031)),
        }




# Formulaire pour la chambre
class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['type_chambre', 'prix_journalier']
        widgets = {
            'prix_journalier': forms.NumberInput(attrs={'step': '0.01'}),  # Pour afficher les champs de prix correctement
        }