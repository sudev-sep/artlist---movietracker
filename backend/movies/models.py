from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class wishlist(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    tmdb_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'tmdb_id'], name='unique_user_wishlist')
        ]

    def __str__(self):
        return f"{self.tmdb_id})"

    
    


class watchedlist(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    tmdb_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'tmdb_id'], name='unique_user_watched')
        ]

    def __str__(self):
        return f"Watched: {self.tmdb_id}"
