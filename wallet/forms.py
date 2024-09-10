from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['balance']


class TransferForm(forms.Form):
    recipient_wallet = forms.IntegerField(label='Recipient Wallet ID')
    amount = forms.PositiveIntegerField(max_digits=10, label='Amount')