from django.db import models
from datetime import date, timedelta
# Create your models here.

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('platinum', 'Platinum'),
        # Add more plans as needed
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    subscription_id=models.AutoField(primary_key=True)
    plan_type = models.CharField(max_length=10, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subscription {self.subscription_id} - {self.plan_type}"

    def remaining_duration(self):
        """Calculate the remaining days for this subscription."""
        today = date.today()
        if self.end_date < today:
            return 0
        return (self.end_date - today).days

    def is_expiring_soon(self, days=2):
        """Check if the subscription is expiring within the next `days` days."""
        return self.remaining_duration() == days