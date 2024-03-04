from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii

def decrypt(ciphertext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ciphertext) + decryptor.finalize()
    return pt

def unpad(data, size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return unpadded_data

ciphertext = input("Enter the ciphertext in hexadecimal format: ")
password = input("Enter the key: ")
key = hashlib.sha256(password.encode()).digest()

ciphertext = binascii.unhexlify(ciphertext)

plaintext = decrypt(ciphertext, key, modes.ECB())
plaintext = unpad(plaintext)

print("Decrypted plaintext:", plaintext.decode())
