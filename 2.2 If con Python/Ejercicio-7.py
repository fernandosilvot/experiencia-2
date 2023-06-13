"""
Se pide identificar el tipo de triángulo, para ello, ingrese el lado a, b y c, luego indique si es isósceles, equilátero o rectángulo.
Es isósceles, si dos lados son iguales.
Es equilátero, si sus tres lados son iguales.
Es escaleno, sus tres lados son diferentes.

"""
lado_a = int(input("Ingrese el lado a: "))
lado_b = int(input("Ingrese el lado b: "))
lado_c = int(input("Ingrese el lado c: "))
if lado_a == lado_b and lado_a == lado_c:
    print("El triángulo es equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
