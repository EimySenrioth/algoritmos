import pandas as pd
import time
import matplotlib.pyplot as plt
#para la impresion de datos, medir los tiempos de ejecucion y graficar
a = []
#lista donde se almaceneran los datos
def prime_tester(n):
    t = 2  # Comenzamos desde 2, pues con 1 no se puede
    while not (n % t == 0 or t == n - 1):
        a.append([t, "F" if n % t != 0 else "T", "T" if t == n - 1 else "F", "---"])
        t += 1  
    
    if n % t == 0:
        a.append([t, "T", "F", f"{t} is a proper divisor of {n}"])  
    else:
        a.append([t, "F", "F", f"{n} is prime"])  
#se inicia con 2 y "F" si t no divide a n, "T" si lo divide. "T" si t=n-1, "F" si no, "---" para si n es primo o no
#una vez que se termina el while, se comprueba si t divide a n, si es asi se imprime que t es divisor de n, si no, se imprime que n es primo
n = int(input("Enter a number: "))
start_time = time.time()
prime_tester(n)
end_time = time.time()
elapsed_time = end_time - start_time
#se solicita el numero, se inicia el cronometro, se ejecuta la funcion y se detiene el cronometro

df = pd.DataFrame(a, columns=["t", "t|n", "t = n - 1", "output"])
#se crea un dataframe con los datos con columnas, t|n: Indica si t divide a n (T o F), t = n - 1: Indica si t = n - 1 (T o F), output: Mensaje de salida si es primo o divisor
print("\nt t|n t = n - 1 output")
print("1 --- --- ---")
for index, row in df.iterrows():
    print(f"{row['t']} {row['t|n']} {row['t = n - 1']} {row['output']}")
#se formatea la salida de datos y el uno lo obiamos
# Crear la gráfica
t_values = df['t']
time_values = list(range(1, len(t_values) + 1))  # Simulación del tiempo en cada iteración
#extraemos los valores de t del daaframe, lent(t_values) obtiene el número total de elementos
# el range gnera un rango de 1 hasta el total de elementos, que estan en una listay se grafica
plt.figure(figsize=(8, 5))
plt.plot(time_values, t_values, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')
plt.xlabel('Iteraciones')
plt.ylabel('Valor de t')
plt.title(f'Tiempo de ejecución para n={n} ({elapsed_time:.6f} segundos)')
plt.legend()
plt.grid()
plt.show()

