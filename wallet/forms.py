from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['balance']


class TransferForm(forms.Form):
    recipient_wallet = forms.IntegerField(label='Recipient Wallet ID')
    amount = forms.IntegerField(label='Amount')
