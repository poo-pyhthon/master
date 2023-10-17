from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField(default=0.0)

class Transaction(models.Model):
    paid_by = models.ForeignKey(UserProfile, related_name='paid_by', on_delete=models.CASCADE)
    amount = models.FloatField()
    participants = models.ManyToManyField(UserProfile, related_name='participants')


