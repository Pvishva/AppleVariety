from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if necessary
    pass
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('can_view', 'Can view my model'),
            ('can_edit', 'Can edit my model'),
        ]

class AppleVariety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apple_images/')
    description = models.TextField()
    visual_characteristics = models.TextField()
    taste_profile = models.TextField()
    culinary_uses = models.TextField()

    def __str__(self):
        return self.name