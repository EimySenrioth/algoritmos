import pandas as pd

a = []  

def prime_tester(n):
    t = 2  # Comenzamos desde 2, pues con 1 no se puede
    while not (n % t == 0 or t == n - 1):  # Hasta que encontramos un divisor o t == n - 1
        # Agregar el valor de t, "F" o "T" para t|n y "T"/"F" para t = n - 1
        a.append([t, "F" if n % t != 0 else "T", "T" if t == n - 1 else "F", "---"])  # Agregar "output"
        t += 1  
    
    if n % t == 0:
        a.append([t, "T", "F", f"{t} is a proper divisor of {n}"])  
    else:
        a.append([t, "F", "F", f"{n} is prime"])  

n = int(input("Enter a number: "))
prime_tester(n)

df = pd.DataFrame(a, columns=["t", "t|n", "t = n - 1", "output"])

print("\nt t|n t = n - 1 output")
print("1 --- --- ---")
for index, row in df.iterrows():
    print(f"{row['t']} {row['t|n']} {row['t = n - 1']} {row['output']}")

# Caso de pureba n=35
# 5 is a proper divisor of 35
