"""
Ingrese por teclado 10 letras, indique cuantas de ellas son vocales y cuántas son consonantes.
"""
for i in range(10): 
    letra = input("Ingrese una letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("La letra ingresada es una vocal")
    else:
        print("La letra ingresada es una consonante")
    