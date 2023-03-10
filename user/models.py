from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    username = models.CharField(max_length=127, unique=True)
    age = models.IntegerField()
    blocked = models.BooleanField(default=False)
    blocked_at = models.DateTimeField(null=True)
    is_colaborator = models.BooleanField(default=False)
