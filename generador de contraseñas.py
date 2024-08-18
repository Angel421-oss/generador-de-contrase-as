#GENERADOR DE CONTRASEÑAS

import random
import string

# Funcion 
def generate_password(longitud=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(characters)for _ in range(longitud))
    return contrasena

longitud_deseada=int(input("Indique los en numero de caracteres de la contrasena: "))
nueva_contrasena=generate_password(longitud_deseada)
print(f'Esta es tu contrasena --> {nueva_contrasena}')


    