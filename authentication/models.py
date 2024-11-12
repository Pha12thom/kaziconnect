from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields if necessary, like role (client or provider)
    is_client = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)

    def __str__(self):
        return self.username
