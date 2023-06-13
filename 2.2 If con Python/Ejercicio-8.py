"""

La empresa dedicada a la venta de zapatos, ha decidido fabricar zapatos de hombre para la venta online. Los zapatos tienen un valor de $20.000 (cualquier número), pero podría variar según la demanda. 
Si la compra es igual o superior a $40.000 el envío es gratis, en caso contario, debe cancelar un monto extra de $3.000 
Determine el total a pagar por una persona que requiere X cantidad de zapatos.

"""
valor_zapato = int(input("Ingrese el valor del zapato: "))
cantidad_zapatos = int(input("Ingrese la cantidad de zapatos: "))
total_compra = valor_zapato * cantidad_zapatos
if total_compra >= 40000:
    print("El total a pagar es: ", total_compra)
else:
    total_compra = total_compra + 3000
    print("El total a pagar es: ", total_compra)
