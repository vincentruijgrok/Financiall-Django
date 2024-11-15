from django import forms

from .models import Account, Mutation


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name']

class MutationForm(forms.ModelForm):
    class Meta:
        model = Mutation
        fields = ['description', 'otherParty', 'otherPartyAccountNumber', 'category', 'group', 'amount']
