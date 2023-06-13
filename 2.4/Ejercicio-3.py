"""
Ingrese por teclado 5 números enteros positivos, súmelos y muestre el resultado de la suma.
"""
suma = 0
for i in range(5):
    num = int(input("Ingrese un número entero: "))
    suma += num
print("La suma de los números ingresados es", suma)