from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Función para cifrar y luego descifrar con DES
def test_des(data, key, mode, padding):
    # Crear un objeto DES
    cipher = DES.new(key, mode)

    # Cifrar los datos
    ciphertext = cipher.encrypt(pad(data.encode(), DES.block_size, style=padding))

    # Mostrar datos cifrados
    print(f"Ciphertext ({padding}): {binascii.hexlify(ciphertext)}")

    # Descifrar los datos
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size, style=padding).decode()

    # Mostrar datos descifrados
    print(f"Decrypted data ({padding}): {decrypted_data}")

# Datos de muestra
data = "Hello world"
key = b"12345678"  # Clave DES de 8 bytes
mode = DES.MODE_ECB  # Modo de cifrado DES
paddings = ['pkcs7', 'iso7816', 'x923']

# Realizar pruebas con diferentes esquemas de relleno
for padding in paddings:
    print(f"\nUsando el esquema de relleno {padding}:")
    test_des(data, key, mode, padding)