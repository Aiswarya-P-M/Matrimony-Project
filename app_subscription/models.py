from django.db import models
from django.utils import timezone
from datetime import date, timedelta
# Create your models here.

class Subscription(models.Model):
    subscription_id=models.AutoField(primary_key=True)
    plan_type = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subscription {self.subscription_id} - {self.plan_type}"

    def calculate_end_date(self, start_date):
        # Handle the duration and calculate the end date
        if 'month' in self.duration:
            months = int(self.duration.split()[0])  # Extract number of months
            end_date = start_date + timedelta(days=30 * months)  # Approximate 30 days per month
        elif 'day' in self.duration:
            days = int(self.duration.split()[0])  # Extract number of days
            end_date = start_date + timedelta(days=days)
        else:
            raise ValueError(f"Invalid duration format: {self.duration}")
        return end_date

    def is_expiring_soon(self, days=2):
        # Check if the subscription is expiring soon (within `days` days)
        if not self.is_active:
            return False
        current_date = timezone.now().date()
        return self.calculate_end_date(self.created_on).date() <= current_date + timedelta(days=days)