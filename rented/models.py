from django.db import models
import uuid


class Rented(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    rented_at = models.DateField()
    devolution_at = models.DateField()
    copy = models.ForeignKey('copies.Copies', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
