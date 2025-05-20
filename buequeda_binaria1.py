
def busqueda_binaria(lista=None, objetivo=None):
    """
    Búsqueda binaria tradicional.
    Muestra cada paso del algoritmo (versión del libro).
    
    Parámetros:
    - lista: Lista ordenada donde buscar
    - objetivo: Elemento a buscar
    
    Retorna:
    - El índice donde se encuentra el elemento o -1 si no está
    """
    # Validaciones
    if lista is None:
        lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        print(f"🔢 Usando lista predeterminada: {lista}")
    
    if objetivo is None:
        objetivo = int(input("🔍 Ingrese el número a buscar: ").strip())
    
    # Verificar si la lista está ordenada
    if any(lista[i] > lista[i+1] for i in range(len(lista)-1)):
        print("⚠️ ADVERTENCIA: La lista no está ordenada. Los resultados pueden ser incorrectos.")
    
    print(f"\n🔎 Buscando {objetivo} en la lista {lista}")
    
    p = 0                         # índice inicial (Python usa índice desde 0)
    q = len(lista) - 1            # índice final

    paso = 1
    while p <= q:
        j = (p + q) // 2
        print(f"🔁 Paso {paso}: p = {p}, j = {j}, q = {q}, A[j] = {lista[j]}")

        if lista[j] == objetivo:
            print(f"✅ Encontrado: {objetivo} está en A[{j}]\n")
            return j
        elif lista[j] < objetivo:
            p = j + 1
        else:
            q = j - 1

        paso += 1

    print(f"❌ {objetivo} no está en la lista.\n")
    return -1

def main():
    """Función principal que ejecuta ejemplos de búsqueda binaria"""
    print("📚 ALGORITMO DE BÚSQUEDA BINARIA 📚")
    print("=" * 40)
    
    # Ejemplo 1: Lista predeterminada
    lista_ejemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"🧪 Ejemplo 1: Lista ordenada {lista_ejemplo}")
    
    while True:
        print("\n📋 Opciones:")
        print("  1. Buscar un número en la lista predeterminada")
        print("  2. Ingresar una nueva lista")
        print("  0. Salir")
        
        opcion = input("\n➤ Su elección: ").strip()
        
        if opcion == "0":
            print("👋 Volviendo al menú principal...")
            break
        elif opcion == "1":
            objetivo = int(input("🔍 Ingrese el número a buscar: ").strip())
            resultado = busqueda_binaria(lista_ejemplo, objetivo)
            if resultado >= 0:
                print(f"📍 El número {objetivo} está en la posición {resultado}")
            else:
                print(f"❓ El número {objetivo} no se encontró en la lista")
        elif opcion == "2":
            try:
                entrada = input("📝 Ingrese los elementos de la lista separados por espacios: ").strip()
                nueva_lista = [int(x) for x in entrada.split()]
                
                if not nueva_lista:
                    print("⚠️ La lista está vacía")
                    continue
                
                # Verificar si está ordenada
                ordenada = all(nueva_lista[i] <= nueva_lista[i+1] for i in range(len(nueva_lista)-1))
                if not ordenada:
                    ordenar = input("⚠️ La lista no está ordenada. ¿Desea ordenarla? (s/n): ").strip().lower()
                    if ordenar in ['s', 'si', 'sí', 'y', 'yes']:
                        nueva_lista.sort()
                        print(f"✅ Lista ordenada: {nueva_lista}")
                    else:
                        print("⚠️ La búsqueda binaria requiere una lista ordenada. Los resultados pueden ser incorrectos.")
                
                objetivo = int(input("🔍 Ingrese el número a buscar: ").strip())
                resultado = busqueda_binaria(nueva_lista, objetivo)
                if resultado >= 0:
                    print(f"📍 El número {objetivo} está en la posición {resultado}")
                else:
                    print(f"❓ El número {objetivo} no se encontró en la lista")
            except ValueError:
                print("❌ Error: Ingrese solo números separados por espacios")
        else:
            print("❌ Opción inválida")
            
    return "Búsqueda binaria completada"

if __name__ == "__main__":
    main()
