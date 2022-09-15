# How to use Bitcoin as one of your payment methods!

This code provides you with a "One use wallet" for Bitcoin and a way for you to easily convert fiat currency to Bitcoin and to validate payments.

<b>FIAT2BTC.py</b> is responsible for converting fiat to bitcoin value. Using simple json request from coindesk api (https://www.coindesk.com/)
<br>
This function takes in two inputs, amount (int) and currency (str). <br>
Amount stands for the amount of money it would cost and currency for the currency in which amount was presented

<b>check_balance.py</b> is responsible for checking the current balance on a given Bitcoin wallet. This as well uses a simple json request. (https://www.blockchain.com/)
<br>
This function needs only the public key (str) and returns the total amount of Bitcoin in the given wallet.
<br>
<br>
<b>generate_wallet.py</b> is responsible for generating a Bitcoin wallet for you and providing a Native segwit address, Private Key and WIF (Wallet Import Format) key.
This function needs no inputs and it returns a Native Segwit Address (Public Key), Private Key and the WIF. 
<br>
<b>It is important not to share your Private Key or the WIF with anybody!</b>

You can check the <b>example.py</b> to see an example of how the code could be constructed. You can see below stdout from the example.py
<br>

    Your total for the painting is: 560€
    Amount to be paid in BTC: 0.028973314
    Send your payment here: bc1q8ypp6uj3xwpa3hfcfg5lwchlctd26vxq6365cq
    Current status for the payment: The payment has not been made.
    




