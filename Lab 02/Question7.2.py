from Crypto.Cipher import ChaCha20
import binascii

key = "qwerty".encode('utf-8') + b"\0" * (32 - len("qwerty".encode('utf-8')))
nonce = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

streams = [
    b'e81461e995',
    b'eb057fe49e34',
    b'e8127ee691315e',
    b'fb0562f592304385d4'
]

for stream in streams:
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = binascii.unhexlify(stream)
    plaintext = cipher.decrypt(ciphertext)
    print("The encrypted message is: ", stream, "And decrypted plaintext is:", plaintext.decode())