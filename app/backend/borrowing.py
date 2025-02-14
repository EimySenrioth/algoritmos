import pandas as pd

a = []
b = []
c = []
d = []
# en a y b se almacenas valores del usur, en c resultados del minunedo y del sustranedo
def borrow_method():
    """Solicita al usuario ingresar el minuendo y el sustraendo."""
    while True:
        try:
            numero_A = int(input("Ingrese el minuendo: "))
            numero_B = int(input("Ingrese el sustraendo: "))

            a.append(numero_A)
            b.append(numero_B)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

def minuendo(numero):
    """Separa decenas y unidades del minuendo, aplicando el préstamo si es necesario."""
    decena, unidad = divmod(numero, 10)
    resta = decena - 1
    suma = unidad + 10  
    c.append([resta, suma])  
#el divmode divide el numero en decenas y unidades, ademas se sigue los pasos de la resta
def sustraendo(numero):
    """Separa decenas y unidades del sustraendo."""
    decena, unidad = divmod(abs(numero), 10)
    d.append([decena, unidad])  
# lo mismo del paso anterior pero el target es el segundo valor del user

borrow_method()
minuendo(a[0])  
sustraendo(b[0])  
#llamamos metodos

df = pd.DataFrame(c, columns=['minuendo_1', 'suma_2'])
#creamos un dataframe con los valores de c en formto de tabla

df_sustraendo = pd.DataFrame(d, columns=['sustraendo_1', 'sustraendo_2'])
df = pd.concat([df, df_sustraendo], axis=1)  
#añadimos los valores de d al dataframe y los concatenamos, osea los unimos
df_resta_prestado_1 = df['minuendo_1'] - df['sustraendo_1']
df_resta_prestado_2 = df['suma_2'] - df['sustraendo_2']
df_suma = pd.concat([df_resta_prestado_1, df_resta_prestado_2], axis=1)
#restamos los valores de los dataframes y los concatenamos
print(df)
print(df_resta_prestado_1)
print(df_resta_prestado_2)
print(df_suma)
print(f"Decena: {df['minuendo_1'][0]}, Unidad: {df['suma_2'][0]}")  