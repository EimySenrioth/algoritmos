import pandas as pd

def n_cast_9():
    while True:
        try:
            numero_A = int(input("Ingrese número a dividir por 9: "))
            return numero_A  
        except ValueError:
            print("Por favor, ingrese un número válido.")

def cast_9(numero):
    digitos = [] #separar todos los numeros
    while numero > 0:
        numero, resul = divmod(numero, 10)  
        digitos.append(resul)  
    return digitos[::-1]#  como los extraje del mas sifnificante al menor los volteo

def sum_cast(digitos):
    suma = sum(digitos)
    return suma
def second_sum_cast(digitos):
    suma = sum(digitos)
    while suma >= 10:
        suma = sum(int(digit) for digit in str(suma))
    return suma

def verificar_divisibilidad_9(suma):
    if suma == 9 or suma % 9 == 0:
        print(f"El número se puede dividir por 9")
        return True
    else:
        print(f"El número no se puede dividir por 9")
        return False

numero = n_cast_9()  
digitos = cast_9(numero)  

df = pd.DataFrame([digitos], columns=[f"A{i}" for i in range(len(digitos))])

print("Dígitos separados:", digitos)
resultado = second_sum_cast(digitos)
print("La suma de los dígitos es:", resultado)

suma_digitos = sum_cast(digitos)
print(f"Suma de los dígitos: {suma_digitos}")
verificar_divisibilidad_9(suma_digitos)
