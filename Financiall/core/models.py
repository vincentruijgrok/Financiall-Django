import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username}) €{self.calculated_balance}"

    @property
    def mutations(self):
        return Mutation.objects.filter(account=self).order_by("-dateTime")

    @property
    def latest_mutation(self):
        return self.mutations.first()

    @property
    def calculated_balance(self):
        return self.mutations.aggregate(Sum('amount'))["amount__sum"] or 0


class Mutation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=256)
    otherParty = models.CharField(max_length=64)
    otherPartyAccountNumber = models.CharField(max_length=64)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    dateTime = models.DateTimeField(auto_now=False)