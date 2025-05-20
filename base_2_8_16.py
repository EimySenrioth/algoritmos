def convertir_base(numero, base): 
    """ 
    Convierte un número decimal a cualquier base especificada (2-16)
    """
    if numero == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    resultado = ""
    signo = ""

    if numero < 0:
        signo = "-"
        numero = abs(numero)

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero = numero // base

    return signo + resultado

def mostrar_explicacion():
    """
    Muestra una explicación del algoritmo y ejemplos
    """
    print("\n📘 CONVERSIÓN A DIFERENTES BASES NUMÉRICAS")
    print("=" * 50)
    print("Este algoritmo convierte un número decimal a:")
    print("  • Binario (base 2)")
    print("  • Octal (base 8)")
    print("  • Hexadecimal (base 16)")
    print("\n📝 EJEMPLO:")
    print("Para convertir 322 a octal (base 8):")
    print("  1. 322 ÷ 8 = 40, resto 2")
    print("  2. 40 ÷ 8 = 5, resto 0")
    print("  3. 5 ÷ 8 = 0, resto 5")
    print("  4. Resultado: 502 (octal)")

def algoritmo_conversion_base():
    """
    Ejecuta la conversión a binario, octal y hexadecimal desde una función
    externa compatible con menú dinámico.
    """
    mostrar_explicacion()
    
    while True:
        try:
            numero = int(input("\n🔢 Ingrese un número entero para convertir: "))
            break
        except ValueError:
            print("❌ Error: Por favor, ingrese un número entero válido.")

    binario = convertir_base(numero, 2)
    octal = convertir_base(numero, 8)
    hexadecimal = convertir_base(numero, 16)

    print("\n✅ RESULTADOS:")
    print("═" * 40)
    print(f"▶ Decimal:     {numero}")
    print(f"▶ Binario:     {binario} (base 2)")
    print(f"▶ Octal:       {octal} (base 8)")
    print(f"▶ Hexadecimal: {hexadecimal} (base 16)")

    return {
        "decimal": numero,
        "binario": binario,
        "octal": octal,
        "hexadecimal": hexadecimal
    }
if __name__ == "__main__":
    algoritmo_conversion_base()