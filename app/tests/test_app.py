import pytest

from app import app

ok_requests = [
    ({'crypto': 'bitcoin', 'fiat': 'usd', 'crypto_amount_to_convert': 20}, 200),
    ({'crypto': 'dogecoin', 'fiat': 'eur', 'crypto_amount_to_convert': 0}, 200),
    ({'crypto': 'solana', 'fiat': 'mxn', 'crypto_amount_to_convert': -40}, 200),
    ({'crypto': 'ethereum', 'fiat': 'pln', 'crypto_amount_to_convert': 20.3}, 200),
    ({'crypto': 'safemoon', 'fiat': 'czk', 'crypto_amount_to_convert': 20.35}, 200)
]

bad_requests = [
    ({}, 400),
    ({'crypto': 'bitcoin', 'fiat': 'usd', 'crypto_amount_to_convert': 'error'}, 400),
    ({'crypto': 'bitcoin', 'fiat': 'error', 'crypto_amount_to_convert': 20}, 400),
    ({'crypto': 'error', 'fiat': 'usd', 'crypto_amount_to_convert': 20}, 400),
    ({'crypto': 'bitcoin', 'fiat': 'usd'}, 400),
    ({'fiat': 'usd', 'crypto_amount_to_convert': 20}, 400),
    ({'crypto': 'bitcoin', 'crypto_amount_to_convert': 20}, 400)
]


@pytest.mark.parametrize('params, expected_status_code', ok_requests)
def test_ok_requests(params, expected_status_code):
    client = app.test_client()
    response = client.get("/convert", query_string=params)

    # test status code response
    assert response.status_code == expected_status_code

    json_data = response.get_json()

    # assert returned data type is correct
    assert isinstance(json_data, dict)

    # assert length of returned data and datatypes are correct
    assert len(json_data) == 6
    assert isinstance(json_data['crypto'], str)
    assert isinstance(json_data['fiat'], str)
    assert isinstance(json_data['datetime'], str)
    assert isinstance(json_data['rate'], (float, int))
    assert isinstance(json_data['fiat_amount'], (float, int))
    assert isinstance(json_data['crypto_amount'], (float, int))

    # assert converted amount is correct
    crypto_amount = json_data['crypto_amount']
    rate = json_data['rate']
    fiat_amount = json_data['fiat_amount']
    assert fiat_amount == round((crypto_amount * rate), 2)


@pytest.mark.parametrize('params, expected_status_code', bad_requests)
def test_bad_requests(params, expected_status_code):
    client = app.test_client()
    response = client.get("/convert", query_string=params)

    # test status code response
    assert response.status_code == expected_status_code

    # test if converted amount is correct
    json_data = response.get_json()
    assert len(json_data) == 1
    assert isinstance(json_data, dict)
    assert isinstance(json_data['message'], str)
