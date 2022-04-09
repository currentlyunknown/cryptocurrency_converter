# Cryptocurrency Converter API

This app creates an endpoint converting the chosen cryptocurrency into fiat of your choice.<br>
It saves the exchange rate request with additional info in your local PostgreSQL database.<br>
Exchange rates based on CoinGecko's API<br>
Stack used: Flask, PostgreSQL, pytest (for testing)<br>


# Installing

- git clone "repository" .
- add an .env file with the following data:
```bash
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
DATABASE_URL
```

# Using the endpoint

##### "/convert"  -  method GET
You have to pass the following parameters:
- crypto: full name of cryptocurrency you want to convert from<br>
- fiat: 3-letter code of fiat you want to convert to<br>
- crypto_amount_to_convert: the amount of crypto you want to convert

Example request:
/convert?crypto=bitcoin&fiat=usd&crypto_amount=55

Example response in JSON format:
{
  "crypto": "bitcoin", 
  "crypto_amount": 55.0, 
  "datetime": "Sat, 09 Apr 2022 21:43:11 GMT", 
  "fiat": "usd", 
  "fiat_amount": 2339645.0, 
  "rate": 42539
}

import requests

url = 'http://127.0.0.1:5000/convert?crypto=dogecoin&fiat=usd&crypto_amount_to_convert=300'
response = requests.get(url)