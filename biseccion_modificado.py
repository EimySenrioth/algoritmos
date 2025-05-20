
def ecuacion(x):
    """Calcula x³ + 2x para un valor dado de x"""
    return x**3 + 2*x

def nbisecc(a=5, b=10, t=200, d=0.005):
    """
    Método de bisección para encontrar x donde ecuacion(x) = t
    
    Parámetros:
    a: límite inferior del intervalo (predeterminado: 5)
    b: límite superior del intervalo (predeterminado: 10)
    t: valor objetivo (predeterminado: 200)
    d: criterio de convergencia (predeterminado: 0.005)
    
    Retorna:
    z: valor de x que satisface ecuacion(x) = t con precisión d
    """
    # Verificar valores iniciales
    fa = ecuacion(a) - t
    fb = ecuacion(b) - t
    
    # Verificar si el intervalo contiene una raíz
    if fa * fb > 0:
        print(f"❌ Error: El intervalo [{a}, {b}] no contiene la raíz o contiene múltiples raíces.")
        print(f"   f({a}) - {t} = {fa}")
        print(f"   f({b}) - {t} = {fb}")
        print(f"   El producto f({a}) * f({b}) debe ser negativo.")
        return None
    
    # Inicializar variables
    iteraciones = 0
    max_iter = 1000  # Límite de seguridad para evitar bucles infinitos
    print("\n🔍 Buscando donde ecuacion(x) = t...")
    print(f"   Buscando x donde x³ + 2x = {t}")
    print(f"   Intervalo inicial: [{a}, {b}]")
    print(f"   Precisión requerida: {d}")
    print("\n📊 TABLA DE ITERACIONES:")
    print("-" * 70)
    print("| Iter |    a    |    b    |    z    |  f(z)   | f(z) - t | Error  |")
    print("-" * 70)
    
    # Punto medio inicial
    z = (a + b) / 2
    fz = ecuacion(z)
    error = abs(b - a) / 2
    
    # Mostrar iteración inicial
    print(f"| {iteraciones:4d} | {a:7.4f} | {b:7.4f} | {z:7.4f} | {fz:7.4f} | {fz-t:8.4f} | {error:6.4f} |")
    
    # Iteraciones de bisección
    while error >= d and iteraciones < max_iter:
        iteraciones += 1
        fz = ecuacion(z)
        
        # Si ecuacion(z) <= t, actualizar a
        if fz <= t:
            a = z
            fa = fz - t
        # Si no, actualizar b
        else:
            b = z
            fb = fz - t
        
        # Recalcular punto medio
        z_ant = z
        z = (a + b) / 2
        fz = ecuacion(z)
        error = abs(z - z_ant)
        
        # Mostrar iteración actual
        print(f"| {iteraciones:4d} | {a:7.4f} | {b:7.4f} | {z:7.4f} | {fz:7.4f} | {fz-t:8.4f} | {error:6.4f} |")
    
    print("-" * 70)
    
    # Verificar convergencia
    if iteraciones >= max_iter:
        print(f"⚠️ Advertencia: Se alcanzó el límite máximo de iteraciones ({max_iter}).")
    

    print(f"\n✅ RESULTADO:")
    print(f"   Valor de x encontrado: {z:.6f}")
    print(f"   f({z:.6f}) = {ecuacion(z):.6f}")
    print(f"   Error absoluto: {error:.6f}")
    print(f"   Diferencia con valor objetivo: {abs(ecuacion(z) - t):.6f}")
    print(f"   Iteraciones realizadas: {iteraciones}")
    
    return z

# Función principal para ser ejecutada desde el menú
def main():
    """Función principal que solicita parámetros al usuario y ejecuta el método de bisección"""
    print("\n🧮 MÉTODO DE BISECCIÓN NUMÉRICA")
    print("=" * 50)
    print("Este algoritmo encuentra el valor de x donde f(x) = t")
    print("La función f(x) = x³ + 2x")
    
    # Solicitar parámetros al usuario
    print("\n📝 Ingrese los parámetros (o presione Enter para usar valores predeterminados):")
    
    try:
        # Límite inferior
        entrada = input("   Límite inferior a [predeterminado=5]: ").strip()
        a = float(entrada) if entrada else 5
        
        # Límite superior
        entrada = input("   Límite superior b [predeterminado=10]: ").strip()
        b = float(entrada) if entrada else 10
        
        # Valor objetivo
        entrada = input("   Valor objetivo t [predeterminado=200]: ").strip()
        t = float(entrada) if entrada else 200
        
        # Precisión
        entrada = input("   Precisión d [predeterminado=0.005]: ").strip()
        d = float(entrada) if entrada else 0.005
        
        # Validar datos de entrada
        if a >= b:
            print("❌ Error: El límite inferior debe ser menor que el límite superior.")
            return None
        
        if d <= 0:
            print("❌ Error: La precisión debe ser mayor que cero.")
            return None
        
        # Ejecutar algoritmo
        resultado = nbisecc(a, b, t, d)
        

        if resultado is not None:
            print("\n🎯 CONCLUSIÓN:")
            print(f"   El valor de x donde x³ + 2x = {t} es aproximadamente {resultado:.6f}")
        
        return resultado
        
    except ValueError as e:
        print(f"❌ Error: Valor no válido. {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None


if __name__ == "__main__":
    main()