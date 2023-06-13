"""
Genere las 10 primeras tablas de multiplicar, cada una de ellas de 1 a 10.
"""
i = 1
while i <= 10:
    print("Tabla del", i)
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1
    print()
    i += 1
