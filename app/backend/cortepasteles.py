#Cake-Cutting Conundrum
import pandas as pd

a = []
b = []
c = []

def n_pastel():
    while True:
        try:
            numero_A = int(input("Ingrese número de punto: "))
            a.append(numero_A)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
def number_points(a):
    for numero_A in a:
        piezas = (numero_A * (numero_A + 1)) // 2 + 1
        c.append(piezas)


n_pastel()
number_points(a)

df = pd.DataFrame(c, columns=['Número de piezas'])

print(df)



