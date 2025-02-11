#Vercion 1.1 del rpm
#Esta nueva vercion tiene representacion binaria de las sumas de las multipliaciones
import numpy as np
import pandas as pd

a = []
b = []
c = []

def number_rps():
    while True:
        try:
            numero_A = int(input("Ingrese un número: "))
            numero_B = int(input("Ingrese otro número: "))

            if numero_A <= 0 or numero_B <= 0:
                print("El número debe ser mayor a 0.")
                continue

            a.append(numero_A)
            b.append(numero_B)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
            
def rpm_binario(a: int) -> str:
    return np.binary_repr(a, width=32)  
   
def rpm_calculo(a, b):
    while a > 0:
        c.append([a, b])  
        a //= 2  
        b *= 2   

number_rps()
rpm_calculo(a[0], b[0]) 


df = pd.DataFrame(c, columns=['a_1', 'b_2'])

df['a_binario'] = df['a_1'].apply(rpm_binario)
df['b_binario'] = df['b_2'].apply(rpm_binario)

def b_evaluation(df):
    """Suma solo los valores de b_2 donde a_1 es impar."""
    return df[df['a_1'] % 2 == 1]['b_2'].sum()
    
    

def ab_multipliaction_result(a, b):
    """Multiplicación tradicional de los dos números."""
    return a * b

def rpm():
    resultado_multiplicacion = ab_multipliaction_result(a[0], b[0])  
    suma_pares = b_evaluation(df)  
    
    binario_1 = np.binary_repr(resultado_multiplicacion,width=32)
    binario_2 = np.binary_repr(suma_pares,width=32)
    

    print("\nProceso de RPS:")
    print(df)
    print(f"Resultado de la multiplicación en binario: {binario_1}, {resultado_multiplicacion}")
    print(f"Resultado con método RPS (suma de b_2 donde a_1 es impar) en binario: {binario_2}, {suma_pares}")
    print(f"Resultado con método RPS (suma de b_2 donde a_1 es impar): {suma_pares}")
    

    if resultado_multiplicacion == suma_pares:
        print(f"\n Hola, el resultado de tu multiplicación es {resultado_multiplicacion} y el RPS da {suma_pares}.")
    else:
        print("\n No se puede realizar la operación.")

rpm()
