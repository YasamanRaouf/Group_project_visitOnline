from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Wallet
from .forms import WalletForm, TransferForm


def wallet_list(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallet/wallet_list.html', {'wallets': wallets})


def wallet_detail(request, wallet_id):
    wallet = get_object_or_404(Wallet, wallet_id=wallet_id)
    return render(request, 'wallet/wallet_detail.html', {'wallet': wallet})


def create_wallet(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wallet:wallet_list')
    else:
        form = WalletForm()
    return render(request, 'wallet/create_wallet.html', {'form': form})


def transfer_funds(request, wallet_id):
    wallet = get_object_or_404(Wallet, wallet_id=wallet_id)

    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            recipient_id = form.cleaned_data['recipient_wallet']
            amount = form.cleaned_data['amount']

            recipient_wallet = get_object_or_404(
                Wallet, wallet_id=recipient_id)

            if wallet.transfer(recipient_wallet, amount):
                return redirect('wallet:wallet_detail', wallet_id=wallet_id)
            else:
                return HttpResponse("Insufficient funds.", status=400)
    else:
        form = TransferForm()

    return render(request, 'wallet/transfer_funds.html', {'form': form, 'wallet': wallet})
