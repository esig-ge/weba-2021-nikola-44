# Zumeri Faton et Châtelain Dorian
from django.db import models
from django.urls import reverse


# Create your models here.


class Produit(models.Model):
    Categorie_prod = (
        ('Colorés', 'Colorés'),
        ('Permanantés', 'Permanantés'),
        ('Endommagés', 'Endommagés'),
        ('Fins Affaiblis', 'Fins Affaiblis'),
        ('Normaux sains', 'Normaux sains'),
        ('White Silver', 'White Silver'),
        ('Cocoa Brown', 'Cocoa Brown'),
        ('Coral Red', 'Coral Red'),
        ('Saffron Copper', 'Saffron Copper'),
        ('Violet Lavender', 'Violet Lavender'),
        ('Cheveux Stressés', 'Cheveux Stressés'),
        ('En profondeur', 'En profondeur')
    )

    Type_choix = (
        ('Shampoo', 'Shampoo'),
        ('Conditioner', 'Conditioner'),
        ('Treatment', 'Treatment'),
        ('Travel Pack', 'Travel Pack'),
        ('Protector', 'Protector'),
        ('Cream', 'Cream'),
        ('Drops', 'Drops'),
        ('Balm', 'Balm'),
        ('Mist', 'Mist'),
        ('Hydra Oil', 'Hydra Oil'),
        ('Oil', 'Oil'),
        ('Mask', 'Mask'),
        ('Serum', 'Serum'),
    )
    nom = models.CharField(max_length=250)
    type = models.CharField(max_length=250, choices=Type_choix)
    categorie = models.CharField(max_length=250, choices=Categorie_prod)
    image = models.ImageField(null=True, blank=True)
    capacite = models.IntegerField()
    prix_achat = models.DecimalField(decimal_places=2, max_digits=5) #centimes
    prix_vente = models.DecimalField(decimal_places=2, max_digits=5) #centimes
    statut = models.CharField(max_length=250)
    quantite = models.IntegerField()

    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url

    def __str__(self):
        return self.nom
