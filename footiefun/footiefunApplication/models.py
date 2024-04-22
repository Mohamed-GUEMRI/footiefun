from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    num_tel = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=100)
    TYPE_COMPTE_CHOICES = [
        ('player', 'Player'),
        ('owner', 'Owner'),
        ('admin', 'Admin'),
    ]
    type_compte = models.CharField(max_length=20, choices=TYPE_COMPTE_CHOICES)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Stade(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='stade_photos/')
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stade = models.ForeignKey(Stade, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Tournoit(models.Model):
    stade = models.ForeignKey(Stade, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    TYPE_CHOICES = [
        ('2v2', '2 VS 2'),
        ('3v3', '3 VS 3'),
        ('4v4', '4 VS 4'),
    ]
    type_tournoit = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()

class Match(models.Model):
    tournoit = models.ForeignKey(Tournoit, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    id_equipeDomicile = models.IntegerField()
    id_equipeExtérieur = models.IntegerField()
    date_match = models.DateTimeField()
    description = models.TextField()
