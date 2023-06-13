"""
Ingrese un número entero mayor a cero por teclado e indique si es o no “Primo”.
"""
num=int(input("Ingrese un número entero mayor a cero: "))
if num>0:
    for i in range(2,num):
        if num%i==0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")
else:
    print("El número no es primo")
    