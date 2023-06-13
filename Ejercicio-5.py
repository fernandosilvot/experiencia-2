"""
Genere las 10 primeras tablas de multiplicar, cada una de ellas de 1 a 10.
"""
for i in range(1, 11):
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()
