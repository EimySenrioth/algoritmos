a = 5
b = 10 #son los valores iniciales del intervalo de la solucion
d = 0.005 #criterio de convergencia o limite que yo le puse
t = 200 #volar que se busca en la funcion

def ecuacion(x):#escriba la funcion con la que trabajo, definiendola en x
    return x**3 + 2*x

def nbisecc():#la funcion principal
    global a, b #las declaro como globales para modificar su valor dentro de la funcion
    z = (a + b) / 2  #formula del punto medio

    while abs(z - a) >= d:  #creo un while hasta que la diferencia entre z y a sea menor que el criterio de parada en d,  valor absoluto
        if ecuacion(z) <= t: #aqui esta la forma f(z) ≤ t
            a = z #la raiz del intervalo derecho se actuliza
        elif ecuacion(z) >= t: #si la raiz del intervalo izquier f(z) ≥ t
            b = z  #se actualiza la raiz del intervalo izquierdo
        z = (a + b) / 2  #se recalcula z y se repite el proceso hasta llegar a la precision puesta

    return z
d = 0.000000111961771811 #criterio de convergencia o limite que yo le puse
def newtonraiz ():
    a_1 = 144 #punto al cual se quiere calcular la raiz
    b_1 = 10 #primera estimacion de la raiz
    x_1 = (b_1 + (a_1/b_1))/2 #formula de la media del cociente
    while abs(x_1 - b_1) >= d: #se detendra cuan la direcia sea meyor al establecido en d, evitar que se detenga
        b_1 = x_1 #se actualiza
        x_1 = (b_1 + (a_1/b_1))/2 #se recalcula
    return x_1         
    
result = nbisecc()
print(result)

result_2 = newtonraiz()
print(result_2)