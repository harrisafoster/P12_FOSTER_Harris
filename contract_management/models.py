from django.db import models
from django.conf import settings

from client_management.models import Client


class Contract(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, blank=True, null=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Contract {str(self.id)} is between sales contact " \
               f"{str(self.sales_contact.id)} and client {str(self.client.id)}."

    class Meta:
        ordering = ['id']
