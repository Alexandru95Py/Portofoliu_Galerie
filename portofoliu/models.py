from django.db import models

class Proiect(models.Model):
    CATEGORII = [
        ('creion', 'Desene în creion'),
        ('ulei', 'Picturi în ulei'),
        ('portret', 'Portrete'),
        ('ilustratie', 'Ilustrații'),
        ('nft', 'NFT-uri')
    ]

    titlu = models.CharField(max_length=100)
    descriere = models.TextField(blank=True)
    link = models.URLField(blank=True)
    imagine = models.ImageField(upload_to='proiecte/', blank=True)
    categorie = models.CharField(max_length=50, choices=CATEGORII)

    def __str__(self):
        return self.titlu
