from django.db import models

# Create your models here.

class Transaction(models.Model):
    statut = models.CharField(max_length=250, null=True, blank=True)
    reference = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return self.reference
