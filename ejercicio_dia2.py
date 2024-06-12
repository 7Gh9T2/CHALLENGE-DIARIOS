#Tabla de Multiplicar: Escribe un programa que se muestre la tabla de multiplicar de un dado número por el usuario.

numero = int(input("Introducir un número"))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")