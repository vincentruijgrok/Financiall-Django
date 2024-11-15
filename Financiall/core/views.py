from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import AccountForm, MutationForm
from .models import Account


# Create your views here.
@login_required
def index(request: HttpRequest):
    user_accounts = Account.objects.filter(owner=request.user)
    return render(request, 'core/home.html', {
        'accounts': user_accounts
    })

def create_account(request: HttpRequest):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            newAccount = form.save(commit=False)
            newAccount.owner = request.user
            newAccount.save()
            return redirect(reverse('core_home'))
    else:
        form = AccountForm()

    return render(request, 'core/create_account.html', {
        'form': form
    })

def read_account(request: HttpRequest, id: str):
    account = get_object_or_404(Account, pk=id)
    return render(request, 'core/read_account.html', {
        'account': account
    })

def create_mutation(request: HttpRequest, id: str):
    account = get_object_or_404(Account, pk=id)
    if request.method == 'POST':
        form = MutationForm(request.POST)
        if form.is_valid():
            newMutation = form.save(commit=False)
            newMutation.account = account
            return redirect(reverse('read_account', id))
    else:
        form = MutationForm()

    return render(request, 'core/create_mutation.html', {
        'form': form,
        'account': account
    })

