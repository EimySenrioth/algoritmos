from decimal import Decimal, getcontext

# Parte 0: Multiplicación con Decimal
print("=== Parte 0: Multiplicación con Decimal ===")
getcontext().prec = 5
num1 = Decimal("3.14159")
num2 = Decimal("2.71828")
resultado = num1 * num2
print(f"Resultado de la multiplicación: {resultado}\n")

# Parte 1: Aproximación usando float
print("=== Parte 1: Aproximaciones con float ===")
a = 625 / 26
print(f"Valor de A: {a}")

b = []
c = []

def aproximacion(a):
    a_truncado = round(a, 2)
    er = abs(a - a_truncado)
    b.append(er)
    err = (er / a) * 100
    c.append(err)
    print(f"Aproximación 1 (2 decimales): {a_truncado}")
    print(f"Error absoluto: {er}")
    print(f"Error relativo: {err:.6f}%\n")

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

# Parte 2: Aproximaciones con entrada del usuario y Decimal
print("=== Parte 2: Aproximaciones usando Decimal ===")
getcontext().prec = 10

try:
    valor_real_str = input("🔢 Ingresa el valor real (ej. 24.03846154): ").strip()
    truncado_str1 = input("✂️ Ingresa el primer valor truncado (ej. 24.03): ").strip()
    truncado_str2 = input("✂️ Ingresa el segundo valor truncado (ej. 24.0384): ").strip()

    valor_real = Decimal(valor_real_str)
    print(f"\nValor de C (preciso): {valor_real}")

    def aproximacion_decimal(valor, truncado_str):
        truncado = Decimal(truncado_str)
        error_abs = abs(valor - truncado)
        error_rel = (error_abs / valor) * 100 if valor != 0 else 0
        print(f"\nAproximación: {truncado} (truncado)")
        print(f"Error absoluto: {error_abs}")
        print(f"Error relativo: {error_rel:.6f}%")
        if error_rel > 50:
            print("⚠️ El error relativo es muy grande. Verifica el valor ingresado.")

    aproximacion_decimal(valor_real, truncado_str1)
    aproximacion_decimal(valor_real, truncado_str2)

except Exception as e:
    print(f"❌ Error: {e}")

