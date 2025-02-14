import pandas as pd

# Listas para almacenar datos
a = []
b = []
c = []
d = []

def carrying_method():
    """Solicita al usuario ingresar el minuendo y el sustraendo."""
    while True:
        try:
            numero_A = int(input("Ingrese el minuendo: "))
            numero_B = int(input("Ingrese el sustraendo con signo menos: "))

            a.append(numero_A)
            b.append(numero_B)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

def minuendo(numero):
    """Separa decenas y unidades del minuendo, aplicando el préstamo si es necesario."""
    decena, unidad = divmod(numero, 10)
    resta = decena 
    suma = unidad + 10  
    c.append([resta, suma])  

def sustraendo(numero):
    """Separa decenas y unidades del sustraendo."""
    decena, unidad = divmod(abs(numero), 10)
    de_1 = decena + 1
    d.append([de_1, unidad])  


carrying_method()
minuendo(a[0])  
sustraendo(b[0])  


df = pd.DataFrame(c, columns=['minuendo_1', 'suma_2'])


df_sustraendo = pd.DataFrame(d, columns=['sustraendo_1', 'sustraendo_2'])
df = pd.concat([df, df_sustraendo], axis=1)  

df_resta_prestado_1 = df['minuendo_1'] - df['sustraendo_1']
df_resta_prestado_2 = df['suma_2'] - df['sustraendo_2']
df_suma = pd.concat([df_resta_prestado_1, df_resta_prestado_2], axis=1)
print(df)
print(df_resta_prestado_1)
print(df_resta_prestado_2)
print(df_suma)
print(f"Decena: {df['minuendo_1'][0]}, Unidad: {df['suma_2'][0]}")  