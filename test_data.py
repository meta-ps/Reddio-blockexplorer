import json
import requests
from pathlib import Path
import shutil
import django
import os
import sys
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()
BASE_DIR = Path(__file__).resolve().parent.parent

from django.contrib.auth.models import User
from reddio.models import Contract, ContractTxns, User as UserWallet

deleteRequired = True

if deleteRequired:

    path1 = Path(os.path.normpath(str(os.getcwd())+"/config/__pycache__"))
    path2 = Path(os.path.normpath(str(os.getcwd())+"/reddio/migrations"))
    path3 = Path(os.path.normpath(
        str(os.getcwd())+"/reddio/__pycache__"))
    path4 = Path(os.path.normpath(str(BASE_DIR))+"/db.sqlite3")
    path5 = Path(os.path.normpath(str(os.getcwd())+"/db.sqlite3"))

    try:
        shutil.rmtree(path1)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        shutil.rmtree(path2)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        shutil.rmtree(path3)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        os.remove(path5)
    except OSError as e:
        print(e)

    cmd1 = "python manage.py makemigrations"
    cmd2 = "python manage.py makemigrations reddio"
    cmd3 = "python manage.py migrate"
    username = "admin"
    email = "admin1@g.com"
    password = "kk"

    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    User.objects.create_superuser(username, email, password)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


my_data = None
with open("stark_key.json", 'r', encoding='utf-8') as f:
    my_data = json.load(f)


RECORD_BASE_API_URI = ""
DEV_NET = True
keys_length = 0
if DEV_NET:
    RECORD_BASE_API_URI = "https://api-dev.reddio.com/v1/records?stark_key="
    keys_length = 1
else:
    RECORD_BASE_API_URI = "https://api.reddio.com/v1/records?stark_key="
    keys_length = len(my_data['stark_keys'])

# keys_length = len(my_data['stark_keys'])


def handleDepositWithdrawRecord(data):
    contract_address_ = data.get('contract_address')
    contract = Contract.objects.get_or_create(
        contract_address=contract_address_)[0]
    contract.name = data.get('asset_name') if data.get(
        'asset_name') else contract.name
    contract.symbol = data.get('symbol') if data.get(
        'symbol') else contract.symbol
    contract.asset_type = data.get('asset_type')
    contract.save()

    #
    obj = ContractTxns.objects.create(contract_address=contract, asset_id=data.get('asset_id'),
                                      assest_name=data.get('asset_name'),
                                      display_value=data.get('display_value'),
                                      record_type=1,
                                      record_status=data.get('status'),
                                      timestamp=data.get('time'),
                                      amount=data.get('amount'),

                                      )
    return


def handleMintRecord(data):
    contract_address_ = data.get('contract_address')
    contract = Contract.objects.get_or_create(
        contract_address=contract_address_)[0]
    contract.name = data.get('asset_name') if data.get(
        'asset_name') else contract.name
    contract.symbol = data.get('symbol') if data.get(
        'symbol') else contract.symbol
    contract.asset_type = data.get('asset_type')
    contract.save()

    #
    obj = ContractTxns.objects.create(contract_address=contract, asset_id=data.get('asset_id'),
                                      assest_name=data.get('asset_name'),
                                      display_value=data.get('display_value'),
                                      record_type=2,
                                      record_status=data.get('status'),
                                      timestamp=data.get('time'),
                                      amount=data.get('amount'),
                                      token_id=data.get('token_id')
                                      )
    return


def handleTransferFromRecord(data):
    # contract
    contract_address_ = data.get('contract_address')
    contract = Contract.objects.get_or_create(
        contract_address=contract_address_)[0]
    contract.name = data.get('asset_name') if data.get(
        'asset_name') else contract.name
    contract.symbol = data.get('symbol') if data.get(
        'symbol') else contract.symbol
    contract.asset_type = data.get('asset_type')
    contract.save()

    # user
    fromAddr = UserWallet.objects.get_or_create(stark_key=data.get('from'))[0]
    toAddr = UserWallet.objects.get_or_create(stark_key=data.get('to'))[0]

    # TXN
    obj = ContractTxns.objects.create(contract_address=contract, asset_id=data.get('asset_id'),
                                      assest_name=data.get('asset_name'),
                                      display_value=data.get('display_value'),
                                      fromAddr=fromAddr,
                                      toAddr=toAddr,
                                      record_type=3,
                                      record_status=data.get('status'),
                                      timestamp=data.get('time'),
                                      token_id=data.get('token_id')
                                      )

    return


def handleASKOrderRecord(data):
    if (Contract.objects.filter(contract_address=data['order'].get('base_contract_address')).count() == 0):
        base_contract = Contract.objects.get_or_create(contract_address=data['order'].get(
            'base_contract_address'), name=data['order'].get('base_asset_name'), contract_type="ERC20")[0]

    if (Contract.objects.filter(contract_address=data['order'].get('quote_contract_address')).count() == 0):
        quote_contract_address = Contract.objects.get_or_create(contract_address=data['order'].get(
            'quote_contract_address'), name=data['order'].get('quote_asset_name'), contract_type="ERC721")[0]

    obj_contract = Contract.objects.get(contract_address = data['order'].get('base_contract_address'))

    # contract
    # Txn
    obj = ContractTxns.objects.create(contract_address=obj_contract, asset_id=data.get('asset_id'),
                                      base_asset_id=data['order'].get('base_asset_id'), base_asset_name=data['order'].get('base_asset_name'),
                                      base_contract_address=data['order'].get('base_contract_address'), fee_asset_name=data['order'].get('fee_asset_name'),
                                      display_value=data['order'].get('display_price'), fee_taken=data['order'].get('fee_taken'),
                                      fee_token_asset=data['order'].get('fee_token_asset'), price=data['order'].get('price'),
                                      quote_asset_id=data['order'].get('quote_asset_id'), quote_asset_name=data['order'].get('quote_asset_name'),
                                      quote_asset_type=data['order'].get('quote_asset_type'), quote_contract_address=data['order'].get('quote_contract_address'),
                                      record_type=7, record_status=data.get('status'), timestamp=data.get('time')
                                      )

    return


def handleBIDOrderRecord(data):

    # contract
    if (Contract.objects.filter(contract_address=data['order'].get('base_contract_address')).count() == 0):
        Contract.objects.get_or_create(contract_address=data['order'].get(
            'base_contract_address'), name=data['order'].get('base_asset_name'), contract_type="ERC20")[0]

    if (Contract.objects.filter(contract_address=data['order'].get('quote_contract_address')).count() == 0):
        Contract.objects.get_or_create(contract_address=data['order'].get(
            'quote_contract_address'), name=data['order'].get('quote_asset_name'), contract_type="ERC721")[0]

    obj_contract = Contract.objects.get(contract_address = data['order'].get('quote_contract_address'))
    # Txn
    obj = ContractTxns.objects.create(contract_address=obj_contract, asset_id=data.get('asset_id'),
                                      base_asset_id=data['order'].get('base_asset_id'), base_asset_name=data['order'].get('base_asset_name'),
                                      base_contract_address=data['order'].get('base_contract_address'), fee_asset_name=data['order'].get('fee_asset_name'),
                                      display_value=data['order'].get('display_price'), fee_taken=data['order'].get('fee_taken'),
                                      fee_token_asset=data['order'].get('fee_token_asset'), price=data['order'].get('price'),
                                      quote_asset_id=data['order'].get('quote_asset_id'), quote_asset_name=data['order'].get('quote_asset_name'),
                                      quote_asset_type=data['order'].get('quote_asset_type'), quote_contract_address=data['order'].get('quote_contract_address'),
                                      record_type=7, record_status=data.get('status'), timestamp=data.get('time'),
                                      token_id=data['order'].get('token_id')
                                      )

    return


y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x = set()
for i in range(keys_length):
    stark_key = my_data['stark_keys'][i]

    # print(stark_key)
    RECORD_API_URI = RECORD_BASE_API_URI + stark_key

    try:
        response_API = requests.get(RECORD_API_URI)
        data = response_API.text
        myData = json.loads(data)

        # print(len(myData['data']['list']))
        # print(type(myData['data']['list'][0]))
        presentId = 0
        presentId_err = ""
        for j in range(len(myData['data']['list'])):
            record_type = myData['data']['list'][j].get('record_type')
            record_data = myData['data']['list'][j]

            x.add(record_type)
            presentId = record_type
            presentId_err = record_data
            if record_type == 1:
                y[1] = record_data
                handleDepositWithdrawRecord(record_data)
            elif record_type == 2:
                y[2] = record_data
            elif record_type == 3:
                y[3] = record_data
                handleTransferFromRecord(record_data)
            elif record_type == 4:
                handleDepositWithdrawRecord(record_data)
                y[4] = record_data
            elif record_type == 7:
                handleASKOrderRecord(record_data)
                y[7] = record_data
            elif record_type == 8:
                handleBIDOrderRecord(record_data)
                y[8] = record_data
            else:
                y[record_type] = record_data

    except e:
        print(e)
        print(presentId)
        print(presentId_err)


print(x)
print(y)


