import pandas as pd
import math

a = []  # Lista para almacenar factores primos

def prime_tester(n):
    q = n
    t = 2
    while t <= math.floor(math.sqrt(q)):
        while q % t == 0:  # Asegura que toma todos los factores repetidos
            a.append([t, "T", "F", f"{t} is a proper divisor of {q}"])
            q //= t
        t += 1
    if q > 1:  # Si queda un número primo mayor que sqrt(n), lo añadimos
        a.append([q, "T", "F", f"{q} is prime"])

n = int(input("Enter a number: "))
prime_tester(n)

# Mostrar los resultados en un DataFrame de Pandas
df = pd.DataFrame(a, columns=["Factor", "T", "F", "Message"])
print(df)

#prueba con 74382