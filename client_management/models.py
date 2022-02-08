from django.db import models

from django.conf import settings


class Client(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(100)
    landline = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Client {self.id}, {str(self.last_name).upper()} {str(self.first_name).capitalize()}"

    class Meta:
        ordering = ['id']
