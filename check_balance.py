import requests


def check_BTC_balance(address):
    url = (f"https://blockchain.info/address/{address}?format=json")
    response = requests.get(url)
    if response.status_code == 200:
        total = response.json()["final_balance"]
        return total
    else:
        return f'[!] Error: {response.status_code}'
