import requests


def getBTCValue(amount, currency):

    currency = currency.upper()

    url = f'https://api.coindesk.com/v1/bpi/currentprice/{currency}.json'
    response = requests.get(url)
    if response.status_code == 200:
        # Currency needs to be written in upper case letters!
        BTC_VALUE = response.json()['bpi'][str(currency)]['rate_float']
        if BTC_VALUE:
            converted_btc = amount/BTC_VALUE
            # Returns rounded value in 9 decimals accuracy.
            return round(converted_btc, 9)

        else:
            return '[!] Error: Failed to convert amount with BTC_VALUE'
    else:
        return f'[!] Error: {response.status_code}'
