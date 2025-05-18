a = []

def expbin():
    while True:
        try:
            numero_A = int(input("Ingrese número: "))
            a.append(numero_A)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

def expo_binaria(base, exponente):

    if exponente == 0:
        return 1, 0 #formato binario
        
    powers = []  
    exp = exponente
    while exp > 0:
        powers.append(exp & 1)#Si es 1, significa que el número es impar; si es 0, el número es par.
        exp >>= 1#es una operación de asignación por desplazamiento a la derecha. Desplaza los bits de exp una posición a la derecha. 
        #Esto divide exp por 2 y descarta el resto
    powers = powers[::-1]  #pone la lista al revez, reverse the powers, pues se extrae del mas significate al menos y los ponde en el orden correcto
    
    result = base if powers[0] else 1 #Comprueba el primer elemento de la lista de potencias (powers[0]):
             #Si powers[0] es 1, result se establece en base.
             #Si powers[0] es 0, result se establece en 1.
    current = base
    multiplications = 0
    
    for i in range(1, len(powers)):
        current *= current#se multiplica por si misma,
        multiplications += 1 #
        
        if powers[i] == 1: #Esta línea verifica si el elemento actual en la lista de potencias es 1
            result *= current  
            multiplications += 1 #contador de multiplicaciones en mas 1
            
    return result, multiplications

expbin()
for n in a:
    result, mults = expo_binaria(2, n)
    print(f"x^{n} requires {mults} multiplications")



   
   
