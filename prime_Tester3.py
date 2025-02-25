import pandas as pd
import math

a = []  

def prime_tester(n):
    t = 2  # El algoritmo empieza con t = 1
    while not (n % t == 0 or t == math.floor(math.sqrt(n))):  # Condición corregida
        a.append([t, "F", "T" if t == math.floor(math.sqrt(n)) else "F", "---"])
        t += 1  
    
    if n % t == 0:
        a.append([t, "T", "F", f"{t} is a proper divisor of {n}"])  
    else:
        a.append([t, "F", "F", f"{n} is prime"])  

n = int(input("Enter a number: "))
prime_tester(n)

df = pd.DataFrame(a, columns=["t", "t|n", "t = ⌊√n⌋", "output"])

print("\nt t|n t = ⌊√n⌋ output")
print("1 --- --- ---")
for index, row in df.iterrows():
    print(f"{row['t']} {row['t|n']} {row['t = ⌊√n⌋']} {row['output']}")
