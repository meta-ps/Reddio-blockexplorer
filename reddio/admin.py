from django.contrib import admin

from reddio.models import Contract, ContractTxns, User

# Register your models here.
admin.site.register(Contract)
admin.site.register(ContractTxns)
admin.site.register(User)