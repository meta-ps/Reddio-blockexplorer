# ReddioScan

ReddioScan allows you to explore and search the transactions, users, contracts and other activities taking place on Reddio

<li> These are the test stark keys used for the development environment. <a href="https://github.com/meta-ps/Reddio-blockexplorer/blob/ff39fd948f1617c0d9dded20edf09ee85665ba9c/stark_key.json#L2">Link</a>
</li>

<li>
    Reddio Development API used: <a href="https://api-dev.reddio.com/v1/records?stark_key=0x1ada455b26b246260b7fd876429289639d7a0ce5fe295ff2355bd4f4da55e2d">api-dev.reddio.com/v1/records</a>
</li> 

<li>
    Structured DB Schema: <a href="https://github.com/meta-ps/Reddio-blockexplorer/blob/ff39fd948f1617c0d9dded20edf09ee85665ba9c/reddio/models.py#L9">Link</a>
</li>

<li>
Script for Forking devnet live data 
<a href="https://github.com/meta-ps/Reddio-blockexplorer/blob/ff39fd948f1617c0d9dded20edf09ee85665ba9c/test_data.py#L236
">Link</a>
</li>

## Clone this repo

```bash
git clone https://github.com/meta-ps/Reddio-blockexplorer.git
```

### Run

Make sure you have `python` and `Django` install then run

```python
pip install django
pip install django-unixtimestampfield
python manage.py makemigrations reddio
python manage.py migrate
python manage.py runserver
```
## Clean Installation and data
```python
python test_data.py
```
