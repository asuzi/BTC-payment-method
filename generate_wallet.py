import random
import ecdsa
import hashlib
import bech32
import base58


def generate_BTC_wallet():

    # Generate random private key.
    privateKey = (random.getrandbits(256)).to_bytes(
        32, byteorder='little', signed=False)

    # Signing key (ecdsa = Elliptic Curve Digital Signature Algorithm)
    signingKey = ecdsa.SigningKey.from_string(
        privateKey, curve=ecdsa.SECP256k1)

    # Verification key
    verifyingKey = signingKey.get_verifying_key()
    x_cor = bytes.fromhex(verifyingKey.to_string().hex())[:32]
    y_cor = bytes.fromhex(verifyingKey.to_string().hex())[32:]

    # Compressed public key
    if int.from_bytes(y_cor, byteorder='big', signed=True) % 2 == 0:
        publicKey = bytes.fromhex(f'02{x_cor.hex()}')
    else:
        publicKey = bytes.fromhex(f'03{x_cor.hex()}')

    # Keyhash
    sha256_key = hashlib.sha256(publicKey)
    ripemd160_key = hashlib.new('ripemd160')
    ripemd160_key.update(sha256_key.digest())
    keyhash = ripemd160_key.digest()

    # Native Segwit
    Natiwe_Segwit_address = bech32.encode('bc', 0, keyhash)

    # Wallet Import Format
    with_80b = bytes.fromhex(f'80{privateKey.hex()}01')
    checksum = hashlib.sha256(hashlib.sha256(with_80b).digest()).digest()[:4]
    WIF = with_80b+checksum
    finished_WIF = base58.b58encode(WIF)

    # Natiwe_Segwit_address is for PublicKey. This is your recieve address. Display it on your payment method page.
    # privateKey.hex() is your private key. Do NOT share it!
    # Finished_WIF.decode("utf-8") is as important as your Private key. Do NOT share this. This is useful for importing the wallets into your own wallet system.

    return Natiwe_Segwit_address, privateKey.hex(), finished_WIF.decode("utf-8")
