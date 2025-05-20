
# Russian Peasant Multiplication

import pandas as pd

def rpm_algorithm():
    """Russian Peasant Multiplication Algorithm - Algoritmo RPS"""
    
    # Listas para almacenar los valores
    a = []
    b = []
    c = []

    def number_rps():
        while True:
            try:
                numero_A = int(input("Ingrese el primer número: "))
                numero_B = int(input("Ingrese el segundo número: "))

                if numero_A <= 0 or numero_B <= 0:
                    print("El número debe ser mayor a 0.")
                    continue

                a.append(numero_A)
                b.append(numero_B)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def rpm_calculo(a_val, b_val):
        while a_val > 0:
            c.append([a_val, b_val])  
            a_val //= 2  
            b_val *= 2   

    def b_evaluation(df):
        """Suma solo los valores de b_2 donde a_1 es impar."""
        return df[df['a_1'] % 2 == 1]['b_2'].sum()

    def ab_multiplication_result(a_val, b_val):
        """Multiplicación tradicional de los dos números."""
        return a_val * b_val

    # Ejecutar el algoritmo
    print("\n=== Russian Peasant Multiplication (RPS) ===")
    number_rps()
    rpm_calculo(a[0], b[0])

    # Crear DataFrame
    df = pd.DataFrame(c, columns=['a_1', 'b_2'])

    # Calcular resultados
    resultado_multiplicacion = ab_multiplication_result(a[0], b[0])  
    suma_pares = b_evaluation(df)  

    print("\nProceso de RPS:")
    print(df)
    print(f"\nNúmeros originales: {a[0]} × {b[0]}")

    if resultado_multiplicacion == suma_pares:
        print(f"\n✓ Resultado correcto!")
        print(f"  Multiplicación tradicional: {resultado_multiplicacion}")
        print(f"  RPS (suma de impares): {suma_pares}")
        return resultado_multiplicacion
    else:
        print("\n✗ Error en el cálculo.")
        return None

# Mantener compatibilidad con tu código original
def number_rps():
    pass

def rpm_calculo(a, b):
    pass

def rpm():
    """Función principal que ejecuta el algoritmo RPS"""
    return rpm_algorithm()

# Permitir ejecución directa del archivo
if __name__ == "__main__":
    rpm_algorithm()
        
        
        








