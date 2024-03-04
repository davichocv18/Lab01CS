from Crypto.Cipher import ARC4
import os
from typing import Union

def main():
    key = os.urandom(16)  # Generate a 128-bit key

    # Example plaintext
    plaintext = b"Hello world"

    # Create an RC4 cipher
    cipher = ARC4.new(key=key)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)

    # Create a new RC4 cipher with the same key for decryption
    new_cipher = ARC4.new(key=key)

    # Decrypt the ciphertext
    decrypted_text = new_cipher.decrypt(ciphertext)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()