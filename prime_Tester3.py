import pandas as pd
import math
import time
import matplotlib.pyplot as plt

a = []  

def prime_tester(n):
    t = 2  # El algoritmo empieza con t = 2
    while not (n % t == 0 or t == math.floor(math.sqrt(n))): 
        a.append([t, "F", "T" if t == math.floor(math.sqrt(n)) else "F", "---"])
        t += 1  
    
    if n % t == 0:
        a.append([t, "T", "F", f"{t} is a proper divisor of {n}"])  
    else:
        a.append([t, "F", "F", f"{n} is prime"])  

n = int(input("Enter a number: "))
start_time = time.time()
prime_tester(n)
end_time = time.time()
elapsed_time = end_time - start_time

df = pd.DataFrame(a, columns=["t", "t|n", "t = ⌊√n⌋", "output"])

print("\nt t|n t = ⌊√n⌋ output")
print("1 --- --- ---")
for index, row in df.iterrows():
    print(f"{row['t']} {row['t|n']} {row['t = ⌊√n⌋']} {row['output']}")


t_values = df['t']
time_values = list(range(1, len(t_values) + 1))  

plt.figure(figsize=(8, 5))
plt.plot(time_values, t_values, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')
plt.xlabel('Iteraciones')
plt.ylabel('Valor de t')
plt.title(f'Tiempo de ejecución para n={n} ({elapsed_time:.6f} segundos)')
plt.legend()
plt.grid()
plt.show()
