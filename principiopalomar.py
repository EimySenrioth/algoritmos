#Ami (chica esquizofrénica) tiene 27 personalidades y cada día puede tener  5 estados de ánimo
#Feliz, Triste, Ansiosa, Enojada y Asustada.
#El objetivo es encontrar el número máximo 
#M de personalidades que pueden tener el mismo estado de ánimo.

p = 27
h = 5
personalidades = p
estados_animo = h

distribucion_base = personalidades // estados_animo

def ami_palomar(p=27, h=5):
    return p//h + (1 if p % h != 0 else 0)#Si el resto no es 0 (es decir, hay un sobrante), entonces se agrega 1 o 0 si no hay sobrante
# tenemos que nos da 5 y sobran 2, que da 6



print(f"El numero de personalidades que pueden tener el mismo estado de animo es: {ami_palomar(p, h)}") 
print(f"El numero de personalidades que pueden tener el mismo estado de animo es y sobran 2: {distribucion_base}")  