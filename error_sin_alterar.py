from decimal import Decimal, getcontext

# Configurar el número de decimales (precisión total de dígitos significativos)
getcontext().prec = 5

# Definir números con precisión exacta
num1 = Decimal("3.14159")
num2 = Decimal("2.71828")

resultado = num1 * num2
print(f"Resultado de la multiplicación: {resultado}")  # Salida esperada: ~8.5397

# Cálculo del valor A
a = 625 / 26
print(f"Valor de A: {a}")

b = []  # Lista para errores absolutos
c = []  # Lista para errores relativos

# Aproximación con 2 decimales
def aproximacion(a):
    a_truncado = round(a, 2)
    er = abs(a - a_truncado)
    b.append(er)
    err = (er / a) * 100
    c.append(err)
    print(f"Aproximación 1 (2 decimales): {a_truncado}")
    print(f"Error absoluto: {er}")
    print(f"Error relativo: {err:.6f}%\n")

# Aproximación con 4 decimales
def aproximacion2(a):
    a_truncado = round(a, 4)
    er = abs(a - a_truncado)
    b.append(er)
    err = (er / a) * 100
    c.append(err)
    print(f"Aproximación 2 (4 decimales): {a_truncado}")
    print(f"Error absoluto: {er}")
    print(f"Error relativo: {err:.6f}%\n")

aproximacion(a)
aproximacion2(a)

# ----------------------------------------------
# Segunda parte: Cálculo de errores usando Decimal y truncados manuales

# Ajustar precisión de contexto
getcontext().prec = 10

# Valor real con precisión decimal
valor_real = Decimal(625) / Decimal(26)
print(f"Valor de C (preciso): {valor_real}")

# Función de aproximación con valor truncado dado como string
def aproximacion(valor, truncado_str):
    truncado = Decimal(truncado_str)
    error_abs = abs(valor - truncado)
    error_rel = (error_abs / valor) * 100 if valor != 0 else 0
    print(f"Aproximación: {truncado} (truncado)")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel:.6f}%\n")

# Evaluar con dos valores truncados
aproximacion(valor_real, "24.03")
aproximacion(valor_real, "24.0384")
