from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.TextField()
    created_at = models.DateTimeField(_("created at"), default=timezone.now)

    def __str__(self) -> str:
        return f"company id: {self.id}"
