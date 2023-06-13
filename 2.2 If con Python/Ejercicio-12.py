"""
Se requiere implementar un sistema para el mesón de CineDuoc, en el cual, va desde el sistema de venta de boletos, hasta los agregados (palomitas y bebidas.). 
Una simulación del sistema comienza con consultar al cliente si pertenece a Duoc (estudiante o funcionario), el cliente muestra la placa o identificación (en caso de tener) por lo que el vendedor registra en el sistema True o False (Pertenece, no pertenece). Luego le consulta que entrada desea: Las posibles entradas son: 
Estreno → $4.800 
Normal → $2.900 

El cliente al seleccionar una, también debe indicar la cantidad que desea, luego el sistema le consultará si desea agregar palomitas de maíz a su pedido, si la respuesta es “si”, entonces el sistema muestra las siguientes promociones: 
Palomitas Pequeña → $2.500 
Palomitas Mediana → $4.500 
Palomitas Grande → $7.800 

Una vez que ingresa el tipo, también debe seleccionar la cantidad.

Finalmente, se le consulta si desea agregar bebidas al sistema de la misma forma: 
Bebida Pequeña → $1.000 
Bebida Mediana → $1.250 
Bebida Grande → $2.000

El sistema deberá mostrar el total a pagar por el cliente, solicitar el efectivo e indicar el vuelto necesario para el cliente. 

Adicionalmente el sistema hará un descuento automático si el cliente pertenece a Duoc, el descuento es de 30% y sólo se aplica a las entradas compradas (no a las Palomitas ni Bebidas).

"""
print("Bienvenido al sistema de venta de boletos")
print("¿Pertenece a Duoc? (S/N): ")
pertenece = input()
if pertenece == "S":
    print("¿Es estudiante o funcionario? (E/F): ")
    tipo = input()
    if tipo == "E":
        pertenece = True
    else:
        pertenece = False
else:
    pertenece = False
print("Seleccione la entrada que desea comprar")
print("1. Estreno")
print("2. Normal")
entrada = int(input())
if entrada == 1:
    entrada = 4800
else:
    entrada = 2900
print("Ingrese la cantidad de entradas que desea comprar")
cant_entradas = int(input())
total = entrada * cant_entradas
print("¿Desea agregar palomitas de maíz? (S/N): ")
palomitas = input()
if palomitas == "S":
    print("Seleccione el tamaño de las palomitas")
    print("1. Pequeña")
    print("2. Mediana")
    print("3. Grande")
    tamano = int(input())
    if tamano == 1:
        tamano = 2500
    elif tamano == 2:
        tamano = 4500
    else:
        tamano = 7800
    print("Ingrese la cantidad de palomitas que desea comprar")
    cant_palomitas = int(input())
    total = total + (tamano * cant_palomitas)
print("¿Desea agregar bebidas? (S/N): ")
bebidas = input()
if bebidas == "S":
    print("Seleccione el tamaño de la bebida")
    print("1. Pequeña")
    print("2. Mediana")
    print("3. Grande")
    tamano = int(input())
    if tamano == 1:
        tamano = 1000
    elif tamano == 2:
        tamano = 1250
    else:
        tamano = 2000
    print("Ingrese la cantidad de bebidas que desea comprar")
    cant_bebidas = int(input())
    total = total + (tamano * cant_bebidas)
if pertenece == True:
    total = total - (total * 0.3)
print("El total a pagar es: ", total)
print("Ingrese el efectivo")
efectivo = int(input())
if efectivo > total:
    vuelto = efectivo - total
    print("El vuelto es: ", vuelto)
elif efectivo < total:
    print("Dinero insuficiente, Guardias!")
else:
    print("Gracias por su compra")
    