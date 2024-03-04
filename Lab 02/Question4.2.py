from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii

def encrypt(plaintext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def pad(data, size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

plaintext = input("Enter the plaintext: ")
password = input("Enter the key: ")
key = hashlib.sha256(password.encode()).digest()

print("Plaintext:", plaintext)

plaintext = pad(plaintext.encode())

ciphertext = encrypt(plaintext, key, modes.ECB())
print("Cipher (ECB):", binascii.hexlify(bytearray(ciphertext)))
