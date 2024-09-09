from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
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
            return redirect('wallet_list')
    else:
        form = WalletForm()
    return render(request, 'wallet/create_wallet.html', {'form': form})

