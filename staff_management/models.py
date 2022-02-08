from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    def __str__(self):
        return f"User {self.id} is {self.username}"

    class Meta:
        ordering = ['id']


class Team(Group):
    def __str__(self):
        return f"Team {self.id}, {str(self.name).capitalize()}"

    class Meta:
        ordering = ['id']
