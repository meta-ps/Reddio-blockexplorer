from django.shortcuts import render
from reddio.models import User, Contract, ContractTxns
# Create your views here.
from django.db.models import Q


def home(request):

    # get latest 10 txns
    # get 10 users
    # get 10 contracts list
    txnCount = ContractTxns.objects.all().count()
    userCount = User.objects.all().count()
    contractCount = Contract.objects.all().count()
    txns = ContractTxns.objects.all().order_by('-timestamp').values()[:15]
    accounts = User.objects.all().values()[:15]
    contracts = Contract.objects.all().values()[:10]

    context = {
        'latestTxns': txns,
        'userAccounts': accounts,
        'txn_count': txnCount,
        'user_count': userCount,
        'contract_count': contractCount
    }

    return render(request, "reddio/index.html", context)


def search_contract(request):
    search_item = request.POST.get('search-field')
    isPresent = False
    obj = {}
    obj2 = {}
    if (Contract.objects.filter(contract_address=search_item).count() != 0):
        isPresent = True
        obj = Contract.objects.get(contract_address=search_item)
        obj2 = ContractTxns.objects.filter(
            contract_address=search_item).order_by('-timestamp').values()

    context = {
        'isPresent': isPresent,
        'contract': obj,
        'contract_txns': obj2
    }

    return render(request, "reddio/contract.html", context)


def user_data(request, pk):

    user_ = User.objects.get(stark_key=pk)

    txn = ContractTxns.objects.filter(fromAddr=user_).order_by(
        '-timestamp') | ContractTxns.objects.filter(toAddr=user_).order_by('-timestamp')

    context = {
        'userTxns': txn.values(),
        'userTxnCount': txn.count(),
        'userAddress': pk
    }

    return render(request, "reddio/user.html", context)
