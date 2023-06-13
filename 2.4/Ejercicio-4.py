"""
Ingrese por teclado un número entero positivo entre 103 y 987, luego genere un proceso que permita invertir el número, 
aplicando las 4 operaciones matemáticas básicas (suma, resta, multiplicación y división). Finalmente, muestre el resultado.
"""
num = int(input("Ingrese un número entero entre 103 y 987: "))
if num>=103 and num<=987:
    num = str(num)
    num = num[::-1]
    num = int(num)
    suma = num + int(num)
    resta = num - int(num)
    multiplicacion = num * int(num)
    division = num / int(num)
    print("La suma de los números invertidos es", suma)
    print("La resta de los números invertidos es", resta)
    print("La multiplicación de los números invertidos es", multiplicacion)
    print("La división de los números invertidos es", division)