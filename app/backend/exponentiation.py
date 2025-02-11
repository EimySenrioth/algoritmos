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
        return 1, 0
        
    powers = []  
    exp = exponente
    while exp > 0:
        powers.append(exp & 1)
        exp >>= 1
    powers = powers[::-1]  
    
    result = base if powers[0] else 1
    current = base
    multiplications = 0
    
    for i in range(1, len(powers)):
        current *= current
        multiplications += 1
        
        if powers[i] == 1:
            result *= current
            multiplications += 1
            
    return result, multiplications

expbin()
for n in a:
    result, mults = expo_binaria(2, n)
    print(f"x^{n} requires {mults} multiplications")



   
   
