"""
Analiza el código con tus compañeros y docente.

Propone otra forma de realizar el enunciado utilizando while.
num = int(input("Ingrese un número entero: "))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print("El factorial de", num, "es", factorial)

"""
num = int(input("Ingrese un número entero: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("El factorial de", num, "es", factorial)
