from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name="Full Name")
    email = models.EmailField(max_length=40, verbose_name="Email")
    contents = models.TextField(max_length=400, verbose_name="Message")
    number = models.CharField(max_length=13, verbose_name="Phone Number")
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Submission Time"
    )
    is_read = models.BooleanField(default=False, verbose_name="Read Status")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact List"
        ordering = ["-created_at"]  # Sort by submission time, newest first

    def __str__(self):
        return (
            f"{self.name} - {self.email} ({self.created_at.strftime('%d/%m/%Y %H:%M')})"
        )
