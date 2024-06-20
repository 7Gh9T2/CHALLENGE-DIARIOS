#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, 
#números y símbolos.

import string
import random

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)
    
    return contrasena

longitud = int(input("Longitud de contraseña deseada: "))

nueva_contrasena = generar_contrasena(longitud)
print("La contraseña segura de 12 caracteres es:", nueva_contrasena)

