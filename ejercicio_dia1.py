
    #Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario.

def invertir_caracteres(cadena_de_caracteres):
    
    if len(cadena_de_caracteres) == 0:
        return ""
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])
print("La cadena invertida es ",invertir_caracteres)
caracteres= input("ingrese una palabra")
cadena_de_caracteres= invertir_caracteres(caracteres)
print("cadena invertida",cadena_de_caracteres)

