#GENERADOR DE CONTRASEÑAS

import random
import string

# Funcion 
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation


    