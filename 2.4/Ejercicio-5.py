"""
Ingresar por teclado 5 números enteros, luego debe indicar:
Cuántos números son mayores a cero
Sume los números pares
Mostrar los resultados

"""
mayores = 0
suma = 0
for i in range(5):
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        mayores += 1
    if num%2 == 0:
        suma += num
print("La cantidad de números mayores a cero es", mayores)
print("La suma de los números pares es", suma)
