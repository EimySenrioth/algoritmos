
# Russian Peasant Multiplication

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

def rpm_calculo(a, b):
    while a > 0:
        c.append([a, b])  
        a //= 2  
        b *= 2   

number_rps()
rpm_calculo(a[0], b[0]) 


df = pd.DataFrame(c, columns=['a_1', 'b_2'])

def b_evaluation(df):
    """Suma solo los valores de b_2 donde a_1 es impar."""
    return df[df['a_1'] % 2 == 1]['b_2'].sum()

def ab_multipliaction_result(a, b):
    """Multiplicación tradicional de los dos números."""
    return a * b

def rpm():
    resultado_multiplicacion = ab_multipliaction_result(a[0], b[0])  
    suma_pares = b_evaluation(df)  

    print("\nProceso de RPS:")
    print(df)

    if resultado_multiplicacion == suma_pares:
        print(f"\n Hola, el resultado de tu multiplicación es {resultado_multiplicacion} y el RPS da {suma_pares}.")
    else:
        print("\n No se puede realizar la operación.")

rpm()

        
        
        








