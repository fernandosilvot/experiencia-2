"""
Considere el caso anterior y aplique:

Try y except donde corresponda
En la opción 1, indique si un número ingresado es par o impar
En la opción 2, muestre la serie Fibonacci de los primeros 10 números
La opción 3, es Salir de la aplicación

"""

def menu():
    print("1. Ingresar un número entero")
    print("2. Mostrar la serie Fibonacci de los primeros 10 números")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def fibonacci():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(8):
        c = a + b
        print(c)
        a = b
        b = c

def par_impar():
    num = int(input("Ingrese un número entero: "))
    if num%2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

def main():
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            try:
                par_impar()
            except ValueError:
                print("Debe ingresar un número entero")
        elif opcion == 2:
            fibonacci()
        else:
            print("Debe ingresar una opción válida")
        opcion = menu()
    print("Fin del programa")

main()
