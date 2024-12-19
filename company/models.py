from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User


class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True
    )  # Ensure one user per company
    name = models.CharField(max_length=80)
    est_date = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ],  # Valid year range
    )
    city = models.CharField(max_length=70, null=True, blank=True)
    state = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.name} - {self.city}, {self.state}"
            if self.name
            else "Unnamed Company"
        )
