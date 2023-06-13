"""
Ingresar por teclado 5 números enteros, luego debe indicar:
Cuántos números son mayores a cero
Cuántos números son menores a cero
Cuántos números son iguales a cero
"""
numeros = []
for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
mayores = 0
menores = 0
iguales = 0
for i in numeros:
    if i > 0:
        mayores += 1
    elif i < 0:
        menores += 1
    else:
        iguales += 1
print("Cantidad de números mayores a cero: ", mayores)
print("Cantidad de números menores a cero: ", menores)
print("Cantidad de números iguales a cero: ", iguales)
