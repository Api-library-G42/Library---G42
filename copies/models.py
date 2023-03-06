from django.db import models
import uuid


class Copies(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_available = models.BooleanField(default=True)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, related_name='copies')