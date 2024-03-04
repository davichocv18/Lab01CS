from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii

def encrypt(plaintext, key, mode):
    method = algorithms.TripleDES(key)  # Change to TripleDES for DES64
    cipher = Cipher(method, mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def pad(data, size=64):  # Adjust padding size for DES64
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

plaintext = input("Enter the plaintext: ")
password = input("Enter the key (must be 8 bytes for DES64): ")
key = hashlib.sha256(password.encode()).digest()[:8]  # Use first 8 bytes for DES64

print("Plaintext:", plaintext)

plaintext = pad(plaintext.encode())

ciphertext = encrypt(plaintext, key, modes.ECB())
print("Cipher (ECB):", binascii.hexlify(bytearray(ciphertext)))