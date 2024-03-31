from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cin = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$', 'Entrez un numéro CIN valide.')])
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=25)
    adresse = models.CharField(max_length=75)
    telephone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Entrez un numéro de téléphone valide.')])
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.cin}'


class Sujet(models.Model):
    TYPE_SUJET_CHOICES = [
        ('TD', 'Travaux Dirigés'),
        ('TPE', 'Travaux Pratiques Encadrés'),
        ('CC', 'Contrôle Continu'),
        ('EXAM', 'Examen'),
    ]
    NIVEAU_CHOICES = [
        ('Niveau 1', 'Niveau 1'),
        ('Niveau 2', 'Niveau 2'),
        ('Niveau 3', 'Niveau 3'),
    ]
    FILIERE_CHOICES = [
        ('INFO', 'Informatique Fondemmentale'),
        ('IGE', 'Informatique et Gestion des Entreprises'),
        ('PHYS', 'Physique'),
        ('CHIM', 'Chimie'),
        ('MATH', 'Mathématiques'),
        ('BIO', 'Science Biologie'),
        ('SCIE', 'Science Environnementale'),
    ]
    nom_cours = models.CharField(max_length=100,)
    code_cours = models.CharField(max_length=10)
    titre = models.CharField(max_length=200)
    type_sujet = models.CharField(max_length=4, choices=TYPE_SUJET_CHOICES)
    annee = models.IntegerField()
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    filiere = models.CharField(max_length=4, choices=FILIERE_CHOICES)
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return f"{self.code_cours} - {self.nom_cours} : {self.titre} ({self.get_type_sujet_display()})"
