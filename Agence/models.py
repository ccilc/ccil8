from django.db import models


# Create your models here.

class Chambre(models.Model):
    """Représente une chambre dans l'hôtel"""

    CHOIX_TYPE_CHAMBRE = [
        ('standard', 'Chambre Standard'),
        ('suite', 'Suite'),
        ('deluxe', 'Chambre Deluxe'),
        ('luxury', 'Chambre de Luxe'),
    ]

    type_chambre = models.CharField(
        max_length=10,
        choices=CHOIX_TYPE_CHAMBRE,
        default='standard'
    )
    prix_journalier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Prix par nuit en euros"
    )

    def __str__(self):
        return f"{self.get_type_chambre_display()} - {self.prix_journalier} €/nuit"

    class Meta:
        verbose_name = "Chambre"
        verbose_name_plural = "Chambres"


class Reservation(models.Model):
    """Représente une réservation effectuée par un client"""

    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Montant total calculé en fonction du prix journalier et du nombre de nuits"
    )

    def save(self, *args, **kwargs):
        # Calculer le nombre de jours de séjour
        delta = self.date_fin - self.date_debut
        delai = delta.days

        # Calculer le montant total
        if delai > 0:
            self.montant_total = self.chambre.prix_journalier * delai
        else:
            self.montant_total = 0

        # Appeler la méthode save() d'origine pour enregistrer l'objet
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Réservation de {self.nom_client} pour {self.chambre} du {self.date_debut} au {self.date_fin}"

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
