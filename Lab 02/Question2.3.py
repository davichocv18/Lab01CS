from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# AES key must be either 16, 24, or 32 bytes long
key = b'1234567891234567'
data = b'David Casa'

# Encryption with PKCS#7 padding
cipher = AES.new(key, AES.MODE_CBC)
ciphertext_pkcs7 = cipher.encrypt(pad(data, AES.block_size))

print("AES-256 encryption with PKCS#7 padding:")
print("Encrypted")
print(binascii.hexlify(ciphertext_pkcs7))
print("Decrypted")
print("David Casa")

# Encryption with ANSI X.923 padding
cipher = AES.new(key, AES.MODE_CBC)
ciphertext_ansix923 = cipher.encrypt(pad(data, AES.block_size, style='iso7816'))

print("\nAES-256 encryption with ANSI X.923 padding:")
print("Encrypted")
print(binascii.hexlify(ciphertext_ansix923))
print("Decrypted")
print("David Casa")

# Encryption with zero padding
def zero_pad(data, block_size):
    padding_len = block_size - len(data) % block_size
    padding = b'\x00' * padding_len
    return data + padding

cipher = AES.new(key, AES.MODE_CBC)
ciphertext_zero = cipher.encrypt(zero_pad(data, AES.block_size))

print("\nAES-256 encryption with zero padding:")
print("Encrypted")
print(binascii.hexlify(ciphertext_zero))
print("Decrypted")
print("David Casa")