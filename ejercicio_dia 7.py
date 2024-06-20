#Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

import random

opciones=["tijera","papel","piedra"]

usuario= input("Elige:"). lower()
ordenador=random.choice(opciones)

if usuario not in opciones:
    print ("Error")
    quit()

if usuario==ordenador:
    print("Empate")

elif usuario=="tijera" and ordenador=="piedra" or usuario=="piedra" and ordenador=="papel" or usuario=="papel"and ordenador=="papel"and ordenador=="tijera":
    print("Has perdido!")

else:
    print("Has ganado")
