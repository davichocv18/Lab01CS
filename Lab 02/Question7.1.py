import os
from typing import Union
from Crypto.Cipher import ChaCha20

class ChaCha20Cipher:
    def __init__(self, key: Union[bytes, str], nonce: Union[bytes, str]):
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(nonce, str):
            nonce = nonce.encode('utf-8')
        self.key = key
        self.nonce = nonce
        self.cipher = ChaCha20.new(key=self.key, nonce=self.nonce)

    def encrypt(self, plaintext: Union[bytes, str]) -> bytes:
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        return self.cipher.encrypt(plaintext)

    def decrypt(self, ciphertext: Union[bytes, str]) -> bytes:
        if isinstance(ciphertext, str):
            ciphertext = ciphertext.encode('utf-8')
        return self.cipher.decrypt(ciphertext)

def main():
    key = input("Enter the key (32 bytes or 256 bits, as a hexadecimal string): ").strip()
    nonce = input("Enter the nonce (12 bytes or 96 bits, as a hexadecimal string): ").strip()

    if len(key) != 64 or len(nonce) != 24:
        print("Invalid key or nonce length. The key must be 32 bytes (256 bits) and the nonce must be 12 bytes (96 bits).")
        return

    try:
        key = bytes.fromhex(key)
        nonce = bytes.fromhex(nonce)
    except ValueError:
        print("Invalid key or nonce format. Please provide hexadecimal strings.")
        return

    cipher = ChaCha20Cipher(key, nonce)

    plaintext = input("Enter the plaintext message: ")
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

    # Crear un nuevo objeto con la misma clave y nonce para descifrar el mensaje
    new_cipher = ChaCha20Cipher(key, nonce)
    decrypted_text = new_cipher.decrypt(ciphertext)

    print("Original message:", plaintext)
    print("Encrypted message:", ciphertext)
    print("Decrypted message:", decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()