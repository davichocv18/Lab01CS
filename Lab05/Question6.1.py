import OpenSSL
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Lista de contraseñas para probar
passwords=["ankle","battery","password","bill","apple","apples","orange"]

# Ruta al archivo PFX
file_path = "fred.pfx"

for password in passwords:
    try:
        # Cargar el archivo PFX
        pfx = open(file_path, 'rb').read()
        
        # Intentar cargar el archivo PFX con la contraseña actual
        p12 = OpenSSL.crypto.load_pkcs12(pfx, password.encode())  # Encode la contraseña a bytes
        print("Contraseña encontrada:", password)

        # Obtener la clave privada y el certificado
        privkey = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey())
        cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate())

        # Convertir el certificado a un objeto x509 de cryptography
        cert = x509.load_pem_x509_certificate(cert, default_backend())

        # Imprimir detalles del certificado
        print(" Issuer:", cert.issuer)
        print(" Subject:", cert.subject)
        print(" Serial number:", cert.serial_number)
        print(" Hash:", cert.signature_hash_algorithm.name)
        print(privkey)

        # No existe la variable 'certificate', usar 'cert' en su lugar
        print(cert)

    except Exception as e:
        # Capturar la excepción y mostrar un mensaje
        print("Contraseña no válida:", password)
