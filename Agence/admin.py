from django.contrib import admin

# Register your models here.

from .models import Chambre, Reservation


#class ReservationAdmin(admin.ModelAdmin):
#    list_display = ('nom_client', 'chambre', 'date_debut', 'date_fin', 'montant_total')
#    search_fields = ('nom_client', 'email_client')
#    list_filter = ('chambre', 'date_debut', 'date_fin')


#admin.site.register(Chambre)
#admin.site.register(Reservation, ReservationAdmin)


# admin.py
class ChambreAdmin(admin.ModelAdmin):
    list_display = ['type_chambre', 'prix_journalier']
    search_fields = ['type_chambre']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['nom_client', 'chambre', 'date_debut', 'date_fin', 'montant_total']
    search_fields = ['nom_client', 'email_client']
    list_filter = ['chambre', 'date_debut']

admin.site.register(Chambre, ChambreAdmin)
admin.site.register(Reservation, ReservationAdmin)