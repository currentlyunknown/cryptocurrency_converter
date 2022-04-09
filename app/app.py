from datetime import datetime

from flask import request, jsonify

from exceptions import CustomException
from models import ExchangeRateRequest
from services import ExchangeRateService
from settings import app, db


@app.route("/convert", methods=["GET"])
def convert():
    crypto = request.args.get("crypto")
    fiat = request.args.get("fiat")
    if crypto is None or fiat is None:
        raise CustomException("Both crypto and fiat are needed")
    try:
        crypto_amount = float(request.args.get("crypto_amount_to_convert"))
    except:
        raise CustomException("Wrong amount to convert")

    utcnow = datetime.utcnow()

    exchanger = ExchangeRateService(crypto=crypto, fiat=fiat)
    exchange_rate = exchanger.download_exchange_rate()
    converted_amount = exchanger.convert_crypto_to_fiat(amount=crypto_amount)

    payload = {
        "crypto": crypto,
        "fiat": fiat,
        "rate": exchange_rate,
        "crypto_amount": crypto_amount,
        "fiat_amount": converted_amount,
        "datetime": utcnow
    }

    entry = ExchangeRateRequest(
        crypto=crypto,
        fiat=fiat,
        datetime=utcnow,
        rate=exchange_rate,
        crypto_amount=crypto_amount,
        fiat_amount=converted_amount,
    )

    db.session.add(entry)
    db.session.commit()

    return jsonify(payload)


if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", port=8000, debug=True)
