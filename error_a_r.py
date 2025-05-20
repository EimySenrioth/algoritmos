from decimal import Decimal, getcontext

def configurar_contexto(precision):
    getcontext().prec = precision

def mostrar_multiplicacion():
    num1 = Decimal("3.14159")
    num2 = Decimal("2.71828")
    resultado = num1 * num2
    print(f"Multiplicación con precisión {getcontext().prec}: {resultado}\n")

def aproximacion_float(a, decimales):
    a_redondeado = round(a, decimales)
    error_abs = abs(a - a_redondeado)
    error_rel = (error_abs / a) * 100
    print(f"Aproximación {decimales} decimales: {a_redondeado}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel:.6f}%\n")

def aproximacion_decimal(valor_real, truncado_str):
    truncado = Decimal(truncado_str)
    error_abs = abs(valor_real - truncado)
    error_rel = (error_abs / valor_real) * 100
    print(f"Aproximación: {truncado} (truncado)")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel:.6f}%\n")

if __name__ == "__main__":
    configurar_contexto(5)
    mostrar_multiplicacion()

    a = 625 / 26
    print(f"Valor de A: {a}\n")

    aproximacion_float(a, 2)
    aproximacion_float(a, 4)

    configurar_contexto(10)
    valor_real = Decimal(625) / Decimal(26)
    print(f"Valor de C (Decimal): {valor_real}\n")

    aproximacion_decimal(valor_real, "24.03")
    aproximacion_decimal(valor_real, "24.0384")
