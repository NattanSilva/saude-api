from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Professional(AbstractUser):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11, unique=True)
    tipoProfissional = models.CharField(max_length=150)
    conselho = models.CharField(max_length=150)
    nomeUSF = models.CharField(max_length=150)
