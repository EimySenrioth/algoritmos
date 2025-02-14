import pandas as pd

a = []
b = []
c = []
d = []

def carrying_method():
    while True:
        try:
            numero_A = int(input("Ingrese el minuendo: "))  
            numero_B = int(input("Ingrese el sustraendo con signo positivo: "))  
            a.append(numero_A)
            b.append(numero_B)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")


def complement_2o(numero):
    """Se calcula el complemento a 9 del sustraendo."""
    decena, unidad = divmod(abs(numero), 10)
    d_d = 9 - decena
    d_n = 9 - unidad
    d.append([d_d, d_n])

def unir_complementos():
    """Une el complemento a 9 y lo devuelve como número completo."""
    nuevo_numero_b = d[0][0] * 10 + d[0][1]
    return nuevo_numero_b

def sum_10(nuevo_numero_b):
    """Suma 1 al complemento a 9 para obtener el complemento a 10."""
    d_10 = nuevo_numero_b + 1
    return d_10

def mat_resultado(a, d_10):
    """Suma el minuendo con el complemento a 10 del sustraendo y resta 100."""
    result = a + d_10 - 100
    return result


carrying_method()

complement_2o(b[0])  

nuevo_numero_b = unir_complementos()  
d_10 = sum_10(nuevo_numero_b)  

resultado = mat_resultado(a[0], d_10)  

print(f"Resultado final: {a[0]} + {d_10} - 100 = {a[0] + d_10} - 100 = {resultado}")
