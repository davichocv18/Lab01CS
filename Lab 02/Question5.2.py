from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib
import binascii

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, DES.block_size)

def unpad(data, size=8):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return unpadded_data

ciphertext = input("Enter the ciphertext in hexadecimal format: ")
password = input("Enter the key: ")
key = hashlib.sha256(password.encode()).digest()[:8]

ciphertext = binascii.unhexlify(ciphertext)

plaintext = decrypt(ciphertext, key)

print("Decrypted plaintext:", plaintext.decode())