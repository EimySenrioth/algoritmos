import pandas as pd

h = []

def mcd(x=10035, y=3568):
    h.clear()  # limpiar historial cada vez que se llama la función
    A = x
    B = y
    R = A % B
    while R > 0:
        h.append([A, B, R, "T" if R > 0 else "F", "T" if R == 0 else "F"])
        A = B
        B = R
        R = A % B
    return B


# Ejemplo de uso
num1 = 10035
num2 = 3568
print(f"MCD de {num1} y {num2} es {mcd(num1, num2)}")

# Mostrar el historial de pasos
df = pd.DataFrame(h, columns=["A", "B", "Residuo", "Residuo > 0", "Residuo = 0"])
print(df)
