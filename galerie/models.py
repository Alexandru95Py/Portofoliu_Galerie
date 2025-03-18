from django.db import models
from django.contrib.auth.models import User

class Tablou(models.Model):
    titlu = models.CharField(max_length=255)
    descriere = models.TextField(default="fara descriere")
    imagine = models.ImageField(upload_to='tablouri/')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titlu
    
class Comentariu(models.Model):
    tablou = models.ForeignKey(Tablou, on_delete=models.CASCADE, related_name="comentarii")
    nume = models.CharField(max_length=255)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentariu de la {self.nume} la {self.tablou.titlu}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilizatorul care dă like
    tablou = models.ForeignKey(Tablou, on_delete=models.CASCADE)  # Tabloul care primește like
    created_at = models.DateTimeField(auto_now_add=True)  # Data și ora like-ului

    class Meta:
        unique_together = ('user', 'tablou')  # Un utilizator poate da like o singură dată per tablou

    def __str__(self):
        return f"{self.user.username} a dat like la {self.tablou.titlu}"


# Create your models here.
