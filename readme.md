/convert?crypto=bitcoin&fiat=usd&crypto_amount=55

import requests

url = 'http://127.0.0.1:5000/convert?crypto=dogecoin&fiat=usd&crypto_amount_to_convert=300'
response = requests.get(url)