from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    password = models.CharField(max_length=60)
    blocked = models.BooleanField(default=False)