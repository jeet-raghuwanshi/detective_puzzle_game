from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavedGameData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_data = models.TextField()  # or other fields as per your requirement

    def __str__(self):
        return f"{self.user.username}'s saved game data"