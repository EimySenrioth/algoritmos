from decimal import Decimal, getcontext

# Configurar el número de decimales que queremos en todas las operaciones
getcontext().prec = 5  # Número total de dígitos significativos

# Definir números con la cantidad exacta de decimales que queremos
num1 = Decimal("3.14159")
num2 = Decimal("2.71828")

resultado = num1 * num2  # Realiza la operación manteniendo la precisión definida

print(resultado)  # Salida: 8.5397

a = 625 / 26
print(f"Valor de A: {a}")

b = []  
c = []  
#redondeado
def aproximacion(a):
    a_truncado = round(a, 2)  # Truncado a 2 decimales
    er = abs(a - a_truncado)  
    b.append(er)
    err = (er / a) * 100  #
    c.append(err)
    print(f"Aproximación 1 (2 decimales): {a_truncado}")
    print(f"Error absoluto: {er}")
    print(f"Error relativo: {err:.6f}%\n")

def aproximacion2(a):
    a_truncado = round(a, 4)  # Truncado a 4 decimales
    er = abs(a - a_truncado)  
    b.append(er)
    err = (er / a) * 100  
    c.append(err)
    print(f"Aproximación 2 (4 decimales): {a_truncado}")
    print(f"Error absoluto: {er}")
    print(f"Error relativo: {err:.6f}%\n")

aproximacion(a)
aproximacion2(a)
#sin redondear y trabaja para las dos aproximaciones
#como el valor que es el orginal y el truncadto str que es el valor truncado
#los prints son para ver el error absoluto y el error relativo

from decimal import Decimal, getcontext
#Decimal es una clase que permite trabajar con números decimales con una precisión arbitraria
# getcontext() devuelve el contexto actual de la clase Decimal
getcontext().prec = 10  

valor_real = Decimal(625) / Decimal(26) #asegurando precisión
print(f"Valor de C: {valor_real}")

def aproximacion(valor, truncado_str):
    truncado = Decimal(truncado_str)
    error_abs = abs(valor - truncado)
    error_rel = (error_abs / valor) * 100 if valor != 0 else 0
    #cadena de texto con el número truncado truncado_str
    # Convierte la cadena en un número Decimal
    # Calcula el error absoluto
    # Calcula el error relativo
    print(f"Aproximación: {truncado} (truncado)")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel:.6f}%\n")

#llamo la funcion con los valores que quiero ya truncados, este trabaja diferente al primerproblema
aproximacion(valor_real, "24.03")  
aproximacion(valor_real, "24.0384")  