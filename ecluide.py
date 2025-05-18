# Definimos la función MCD usando el algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcd_de_tres(a, b, c):
    resultado_parcial = mcd(a, b)
    resultado_final = mcd(resultado_parcial, c)
    return resultado_final

# Solicita tres números al usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

resultado = mcd_de_tres(a, b, c)
print(f"\nEl MCD de {a}, {b} y {c} es: {resultado}")
