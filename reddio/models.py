from django.db import models
from django.utils.translation import gettext_lazy as _
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.
# class User(models.Model):


class User(models.Model):
    walletAddress = models.CharField(max_length=255, null=True, blank=True)
    # A unique key that identifies the user in the off-chain state. users are identified within Reddio by their Stark Key which is a public key defined over starknetcc
    stark_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.stark_key


class Contract(models.Model):
    contract_address = models.CharField(
        unique=True, primary_key=True, max_length=255, blank=True)

    class ContractType(models.TextChoices):
        NONE = 'NONE', _('NONE')
        ERC20 = 'ERC20', _('ERC20')
        ERC721 = 'ERC721', _('ERC721')

    name = models.CharField(max_length=255, null=True, blank=True)
    symbol = models.CharField(max_length=255, null=True, blank=True)
    contract_type = models.CharField(
        max_length=21, choices=ContractType.choices, default=ContractType.NONE)


class ContractTxns(models.Model):
    contract_address = models.ForeignKey(Contract, on_delete=models.CASCADE)

    class RecordType(models.TextChoices):
        DEFAULT = 0, _('DEFAULT')
        DepositRecordType = 1, _('DepositRecordType')
        MintRecordType = 2, _('MintRecordType')
        TransferFromRecordType = 3, _('TransferFromRecordType')
        WithdrawRecordType = 4, _('WithdrawRecordType')
        ASKOrderRecordType = 7, _('ASKOrderRecordType')
        BIDOrderRecordType = 8, _('BIDOrderRecordType')
        #7 TakerAsk - sells the NFT for the ERC-20 token
        #8 MakerBid - user wishes to acquire a NFT using a specific ERC-20 token.

    
    class RecordStatusType(models.TextChoices):
        DEFAULT = 0, _('DEFAULT')
        Submitted = 1, _('Submitted')
        Accepted = 2, _('Accepted')
        Failed = 3, _('Failed')
        Proved = 4, _('Proved')
        ProvedError = 5, _('ProvedError')
    
    asset_id = models.CharField(max_length=255, null=True, blank=True)
    assest_name = models.CharField(max_length=255, null=True, blank=True)
    record_type = models.IntegerField(
        default=RecordType.DEFAULT, choices=RecordType.choices)
    
    display_value = models.CharField(max_length=255, null=True, blank=True)
    timestamp = UnixTimeStampField(use_numeric=True, default=0.0)
    amount = models.CharField(max_length=255, null=True, blank=True)
    record_status = models.IntegerField(
        default=RecordStatusType.DEFAULT, choices=RecordStatusType.choices)
    base_asset_id = models.CharField(max_length=255, null=True, blank=True)
    base_asset_name = models.CharField(max_length=255, null=True, blank=True)
    base_contract_address = models.CharField(
        max_length=255, null=True, blank=True)
    fee_asset_name = models.CharField(max_length=255, null=True, blank=True)
    fee_taken = models.CharField(max_length=255, null=True, blank=True)
    fee_token_asset = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    quote_asset_id = models.CharField(max_length=255, null=True, blank=True)
    quote_asset_name = models.CharField(max_length=255, null=True, blank=True)
    quote_asset_type = models.CharField(max_length=255, null=True, blank=True)
    quote_contract_address = models.CharField(
        max_length=255, null=True, blank=True)
    token_id = models.CharField(max_length=255, null=True, blank=True)
    fromAddr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromAddress', null=True)
    toAddr = models.ForeignKey(User, on_delete=models.CASCADE,related_name='toAddress', null=True)
