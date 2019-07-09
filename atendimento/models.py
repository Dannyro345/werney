from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)