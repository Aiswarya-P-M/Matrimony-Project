from django.db import models
from app_user.models import CustomUser

class Matching(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name='matches_user1', on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(CustomUser, related_name='matches_user2', on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=10,
        choices=[('accepted', 'Accepted'), ('pending', 'Pending'), ('rejected', 'Rejected')],
        default='pending'
    )
    match_score = models.FloatField(null=True, blank=True)  # Store the match score (percentage)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Match between {self.user1.username} and {self.user2.username} - Status: {self.status}"
