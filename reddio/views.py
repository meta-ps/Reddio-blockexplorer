from django.shortcuts import render
from reddio.models import User, Contract, ContractTxns
# Create your views here.


def home(request):
    # mydata = Members.objects.all().order_by('-firstname').values()
    # get latest 10 txns
    # get 10 users
    # get 10 contracts list

    txns = ContractTxns.objects.all().order_by('-timestamp').values()[:15]
    accounts = User.objects.all().values()[:15]
    contracts = Contract.objects.all().values()[:10]

    context = {
        'latestTxns': txns,
        'userAccounts':accounts,
        'contracts':contracts
    }



    return render(request, "reddio/index.html",context)
    