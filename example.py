from BTC2FIAT import getBTCValue
from check_balance import check_BTC_balance
from generate_wallet import generate_BTC_wallet


# You are selling a painting for a 560€
price_EUR = 560

# !!! INVOICE !!!

# You show recieve_wallet to the customer in your invoice page & and save it so you can use this later to check for payments!
# Also you should save your private_key or WIF (or both) so you can access the money you have gained.
recieve_wallet, private_key, WIF = generate_BTC_wallet()

# You need to show how much BTC a customer should pay in BTC for the payment to be fully done.
price_BTC = getBTCValue(price_EUR, 'EUR')

# Now it is time to check if the customer has paid you.
current_BTC_amount = check_BTC_balance(recieve_wallet)

if current_BTC_amount >= price_BTC:
    payment_status = 'The payment has been made.'
elif current_BTC_amount < price_BTC:
    payment_status = 'The payment has not been made.'

# Simple example using print()

print(f'Your total for the painting is: {price_EUR}€')
print(f'Amount to be paid in BTC: {price_BTC}')
print(f'Send your payment here: {recieve_wallet}')
print(f'Current status for the payment: {payment_status}')
