from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from fmanager.fmanager.constants import GoalState


class Card(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=20)
    cvv = models.IntegerField()
    amount = models.FloatField()
    expireDate = models.DateField()

    def __str__(self):
        return self.name


class Goal (models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    state = models.IntegerField(choices=GoalState.CHOICES)
    objective = models.FloatField()
    amountCollected = models.FloatField(default=0)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=500)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, related_name='transactions')
    description = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.name
