from django.db import models

class Api(models.Model):
    first_name = models.CharField("Nome", max_length=30)
    last_name = models.CharField("Sobrenome", max_length=30)
    email = models.CharField("e-mail", max_length=50)
    created_at = models.DateField("Data de Registro",  auto_now_add=True)
    