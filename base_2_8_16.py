def convertir_base(numero, base):
    digitos = "0123456789ABCDEF"  # Para manejar números hexadecimales
    resultado = ""
    #se toma el numero que se quiere convertir y la base a la que se quiere convertir
    #en base 2, 8 y 16 y el resuktado almacena los digitos convertidos
    while numero > 0:
        resultado = digitos[numero % base] + resultado
        numero = numero // base
    #se toma del libro la formula  n=dk​⋅bk+dk−1​⋅bk−1+⋯+d1​⋅b1+d0​⋅b0 y las bases se van cambiando
    #322 ÷ 8 = 40, resto 2.
    #40 ÷ 8 = 5, resto 0.
    #5 ÷ 8 = 0, resto 5.
    return resultado if resultado != "" else "0"  # Si el número es 0, devolvemos "0"

while True:
    try:
        numero_A = int(input("Ingrese un número para convertirlo a representación en 2, 8 y 16: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero.")
#llamamos a las funciones y se cambian las bases
binario_resultado = convertir_base(numero_A, 2)
octal_resultado = convertir_base(numero_A, 8)
hexadecimal_resultado = convertir_base(numero_A, 16)

print(f"El número {numero_A} en binario es: {binario_resultado}")
print(f"El número {numero_A} en octal es: {octal_resultado}")
print(f"El número {numero_A} en hexadecimal es: {hexadecimal_resultado}")


#test 322; 2, 8, 16: 