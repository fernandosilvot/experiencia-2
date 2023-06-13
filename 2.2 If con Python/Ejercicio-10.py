"""
En el contexto del coronavirus, una persona ha decidido fabricar mascarillas lavables para la venta online. Las mascarillas tienen un valor de $500 pero podría variar según la demanda. Si la compra es superior a $15.000 el envío es gratis, en caso contario: 
Si es de la misma comuna el envío es de $1.000 
Si es de una comuna aledaña $2.000 
En otro caso es de $3.000 

Determine el total a pagar por una persona que requiere X cantidad de mascarillas.

"""
valor_mascarilla = int(input("Ingrese el valor de la mascarilla: "))
cantidad_mascarillas = int(input("Ingrese la cantidad de mascarillas: "))
total_compra = valor_mascarilla * cantidad_mascarillas
if total_compra > 15000:
    print("El total a pagar es: ", total_compra)
else:
    comuna = input("Ingrese la comuna: ")
    if comuna == "comuna":
        total_compra = total_compra + 1000
        print("El total a pagar es: ", total_compra)
    elif comuna == "aledaña":
        total_compra = total_compra + 2000
        print("El total a pagar es: ", total_compra)
    else:
        total_compra = total_compra + 3000
        print("El total a pagar es: ", total_compra)
