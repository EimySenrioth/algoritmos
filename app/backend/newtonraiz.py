d = 0.000000111961771811  # criterio de convergencia o límite

def newtonraiz():
    a_1 = 144  # número al cual se quiere calcular la raíz cuadrada
    b_1 = 10   # primera estimación de la raíz
    x_1 = (b_1 + (a_1 / b_1)) / 2  # fórmula de la media del cociente

    while abs(x_1 - b_1) >= d:
        b_1 = x_1
        x_1 = (b_1 + (a_1 / b_1)) / 2

    return x_1

result_2 = newtonraiz()
print(result_2)