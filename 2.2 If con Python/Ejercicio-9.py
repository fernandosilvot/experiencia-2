"""
En un delivery se venden 4 tipos de sándwich: 
Churrasco $1.500 
Completo $1.000 
Vegetariano $2.000 
Barros Luco $3.000 

Determine el total a pagar por un cliente, al indicar la cantidad de sándwiches que llevaría de cada tipo. Considere que si tiene un código de descuento se le realizará sólo un 10% al total de la venta.

"""
churrasco = 1500
completo = 1000
vegetariano = 2000
barros_luco = 3000
total = 0
print("Ingrese la cantidad de sándwiches que llevará de cada tipo")
cant_churrasco = int(input("Churrasco: "))
cant_completo = int(input("Completo: "))
cant_vegetariano = int(input("Vegetariano: "))
cant_barros_luco = int(input("Barros Luco: "))
total = (churrasco * cant_churrasco) + (completo * cant_completo) + (vegetariano * cant_vegetariano) + (barros_luco * cant_barros_luco)
print("El total a pagar es: ", total)
codigo = input("Ingrese el código de descuento: ")
if codigo == "descuento":
    total = total - (total * 0.1)
    print("El total a pagar con descuento es: ", total)
else:
    print("El total a pagar es: ", total)
