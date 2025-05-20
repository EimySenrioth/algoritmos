def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en una lista.
    Retorna el índice si se encuentra el objetivo, o -1 si no.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def main():
    """
    Función principal que se ejecuta desde el menú dinámico.
    Usa una lista de prueba y pide al usuario el valor a buscar.
    """
    print("\n🔎 BUSQUEDA LINEAL")
    print("-" * 40)
    
    lista = [10, 25, 3, 7, 99, 42]
    print(f"Lista actual: {lista}")
    
    try:
        objetivo = int(input("Ingrese el número que desea buscar: "))
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")
        return

    indice = busqueda_lineal(lista, objetivo)

    if indice != -1:
        print(f"✅ El valor {objetivo} se encuentra en la posición {indice}.")
    else:
        print(f"❌ El valor {objetivo} no se encuentra en la lista.")
