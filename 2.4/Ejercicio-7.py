"""
Ingrese un número entero mayor a cero por teclado e indique si es o no “Perfecto”.
"""
num=int(input("Ingrese un número entero mayor a cero: "))
if num>0:
    suma = 0
    for i in range(1,num):
        if num%i==0:
            suma += i
    if suma == num:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
else:
    print("El número no es perfecto")