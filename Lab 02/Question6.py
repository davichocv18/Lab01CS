from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import binascii
import base64

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

ciphertext_base64 = input("Enter the ciphertext in Base-64 format: ")
ciphertext = base64.b64decode(ciphertext_base64)

passwords = ["hello", "ankle", "changeme", "123456"]
for password in passwords:
    key = hashlib.sha256(password.encode()).digest()
    try:
        plaintext = decrypt(ciphertext, key, modes.ECB())
        plaintext = unpad(plaintext)
        print(f"Decrypted plaintext with password '{password}':", plaintext.decode())
    except ValueError as e:
        print(f"Error with password '{password}':", e)