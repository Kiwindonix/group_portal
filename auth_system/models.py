from django.contrib.auth.models import AbstractUser
from django.db import models


def get_default_dict():
    return {
        'theme': 'light',
    }


class CustomUser(AbstractUser):
    settings = models.JSONField(default=get_default_dict)