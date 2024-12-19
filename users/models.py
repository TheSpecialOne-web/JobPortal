from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    # Ajoutez des related_name pour éviter les conflits
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Nom unique pour votre modèle
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Nom unique pour votre modèle
        blank=True,
    )
