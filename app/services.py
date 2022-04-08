import requests

from exceptions import CustomException
from settings import CRYPTO_URL, CONVERT_PRECISION, EXCHANGE_RATE_PRECISION


class ExchangeRateService:

    def __init__(self, crypto, fiat):
        self.crypto = crypto
        self.fiat = fiat

    def download_exchange_rate(self) -> int:
        url = f'{CRYPTO_URL}vs_currency={self.fiat}&ids={self.crypto}'
        response = requests.get(url)
        if not response.ok:
            raise CustomException('Wrong fiat name')
        try:
            rate = response.json()[0]['current_price']
        except IndexError:
            raise CustomException('Wrong crypto name')
        return round(rate, EXCHANGE_RATE_PRECISION)

    def convert_crypto_to_fiat(self, amount) -> float:
        exchange_rate = ExchangeRateService(self.crypto, self.fiat).download_exchange_rate()
        converted_amount = amount * exchange_rate
        return round(converted_amount, CONVERT_PRECISION)
