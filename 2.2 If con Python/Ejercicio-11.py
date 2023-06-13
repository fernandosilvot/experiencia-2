"""
Usted es el encargado de generar un sistema de compra, el cual consiste en:
Seleccionar si desea el producto o no, en el caso de llevar el producto, el total de la compra debe ir aumentando dependiendo de cuantos productos lleve y el valor de cada uno de ellos, también debe ingresar si el cliente es preferencial o no, en el caso de ser preferencial, al final al momento de pagar se debe realizar un descuento del 25% del total de la compra, finalmente se solicita que ingrese el efectivo, debe calcular cuánto es el vuelto del cliente en el caso de que el efectivo sea mayor al total a pagar, del caso contrario verificar que el monto no sea inferior al total a pagar o enviar una salida por pantalla que diga “ Dinero insuficiente, Guardias!”. 
Los productos detallados son los siguientes:
Agua → $ 600 
Azúcar→ $1200 
Aceite → $1500 
Arroz → $1250 
Fideos → $ 790 
Bebida→ $1780 
Chocolate → $2500 
Pan molde → $1340
"""
print("Bienvenido al sistema de compra")
print("Seleccione el producto que desea comprar")
print("1. Agua")
print("2. Azúcar")
print("3. Aceite")
print("4. Arroz")
print("5. Fideos")
print("6. Bebida")
print("7. Chocolate")
print("8. Pan molde")
print("9. Salir")
producto = int(input("Ingrese el producto: "))
total_compra = 0
while producto != 9:
    if producto == 1:
        total_compra = total_compra + 600
    elif producto == 2:
        total_compra = total_compra + 1200
    elif producto == 3:
        total_compra = total_compra + 1500
    elif producto == 4:
        total_compra = total_compra + 1250
    elif producto == 5:
        total_compra = total_compra + 790
    elif producto == 6:
        total_compra = total_compra + 1780
    elif producto == 7:
        total_compra = total_compra + 2500
    elif producto == 8:
        total_compra = total_compra + 1340
    else:
        print("Opción incorrecta")
    producto = int(input("Ingrese el producto: "))
print("El total de la compra es: ", total_compra)
preferencial = input("¿Es preferencial? (S/N): ")
if preferencial == "S":
    total_compra = total_compra - (total_compra * 0.25)
    print("El total a pagar es: ", total_compra)
else:
    print("El total a pagar es: ", total_compra)
efectivo = int(input("Ingrese el efectivo: "))
if efectivo > total_compra:
    vuelto = efectivo - total_compra
    print("El vuelto es: ", vuelto)
elif efectivo < total_compra:
    print("Dinero insuficiente, Guardias!")
else:
    print("Gracias por su compra")
    