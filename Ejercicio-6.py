"""
Genere las tablas de multiplicar de los primeros números pares entre 1 y 10.
"""
for i in range(1, 11):
    if i%2==0:
        print("Tabla del", i)
        for j in range(1, 11):
            print(i, "x", j, "=", i*j)
        print()
