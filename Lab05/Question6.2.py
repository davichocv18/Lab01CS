import OpenSSL

# Lista de frutas y países
fruits = [
    "apple", "orange", "banana", "kiwi", "grape", "melon", "pear", "peach", "plum", "cherry",
    "lemon", "lime", "mango", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry",
    "apricot", "avocado", "coconut", "fig", "guava", "nectarine", "papaya", "passionfruit", "pomegranate",
    "quince", "tangerine", "watermelon", "cranberry", "elderberry", "grapefruit", "kumquat", "lychee", "persimmon",
    "rhubarb", "starfruit", "boysenberry", "cantaloupe", "honeydew", "mulberry", "plantain", "tamarind", "durian"
]
countries = [
    "usa", "uk", "canada", "france", "germany", "spain", "italy", "sweden", "norway", "denmark",
    "finland", "australia", "newzealand", "japan", "china", "india", "brazil", "argentina", "mexico",
    "southafrica", "egypt", "russia", "turkey", "greece", "poland", "thailand", "vietnam", "philippines",
    "singapore", "malaysia", "indonesia", "southkorea", "northkorea", "taiwan", "hongkong", "israel", "iraq",
    "iran", "saudiarabia", "uae", "qatar", "kuwait", "bahrain", "oman", "jordan", "syria", "lebanon",
    "yemen", "afghanistan", "pakistan", "bangladesh", "srilanka", "nepal", "bhutan", "maldives", "mongolia",
    "kazakhstan", "uzbekistan", "tajikistan", "kyrgyzstan", "georgia", "armenia", "azerbaijan", "belarus", "ukraine",
    "moldova", "romania", "bulgaria", "hungary", "serbia", "croatia", "slovenia", "bosnia", "montenegro",
    "albania", "macedonia", "kosovo", "estonia", "latvia", "lithuania", "belgium", "netherlands", "luxembourg",
    "switzerland", "austria", "portugal", "ireland", "iceland", "greenland", "faroe", "cyprus", "malt"
]

# Función para probar las contraseñas
def test_passwords(file_prefix, password_list):
    for i in range(1, 19):  # Iterar sobre los archivos bill01.pfx a bill18.pfx
        file_path = f"{file_prefix}{i:02}.pfx"
        for password in password_list:
            try:
                # Cargar el archivo PFX
                pfx = open(file_path, 'rb').read()

                # Intentar cargar el archivo PFX con la contraseña actual
                p12 = OpenSSL.crypto.load_pkcs12(pfx, password.encode())
                print(f"Contraseña encontrada para {file_path}: {password}")
                break  # Salir del bucle si se encuentra la contraseña

            except Exception as e:
                pass  # Continuar probando contraseñas

# Probar contraseñas para los archivos bill01.pfx a bill18.pfx con la lista de frutas
test_passwords("bill", fruits)

# Probar contraseñas para los archivos country01.pfx a country06.pfx con la lista de países
test_passwords("country", countries)