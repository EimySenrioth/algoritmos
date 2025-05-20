# Librerías utilizadas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.patches as patches

# Configuración para entornos sin GUI
matplotlib.use('Agg')  # Usa un backend sin GUI

def crear_triangulo_pascal(n=11):
    """
    Crea el triángulo de Pascal hasta el nivel n
    
    Parámetros:
    n (int): Número de niveles del triángulo (predeterminado: 11)
    
    Retorna:
    list: Lista de listas con los valores del triángulo de Pascal
    """
    resultado = []
    for i in range(n):
        fila = [1]
        for j in range(1, i):
            fila.append(resultado[i-1][j-1] + resultado[i-1][j])
        if i > 0:
            fila.append(1)
        resultado.append(fila)
    return resultado

def preparar_datos_triangulo(n=11):
    """
    Prepara los datos del triángulo de Pascal para visualización
    
    Parámetros:
    n (int): Número de niveles del triángulo (predeterminado: 11)
    
    Retorna:
    DataFrame: DataFrame con los datos del triángulo de Pascal
    """
    triangulo = crear_triangulo_pascal(n)
    
    # Creo listas vacías para almacenar los datos
    filas = []
    columnas = []
    valores = []
    orientaciones = []  
    
    # Recorro cada fila del triángulo
    for i, fila in enumerate(triangulo):
        for j, valor in enumerate(fila):
            # Ajusto la posición para centrar el triángulo
            col_pos = n - i - 1 + j * 2  
            
            # Agrego datos a las listas
            filas.append(i)
            columnas.append(col_pos)
            valores.append(valor)
            orientaciones.append(j % 2)  # Alterno entre 0 y 1
            
    # Creo un DataFrame con todos los datos
    df = pd.DataFrame({
        'fila': filas,
        'columna': columnas,
        'valor': valores,
        'orientacion': orientaciones,
        'log_valor': np.log1p(valores)  # Logaritmo natural para visualización
    })
    
    return df

def visualizar_triangulo_seaborn(n=11, paleta='YlOrBr', save_file=None):
    """
    Visualiza el triángulo de Pascal con seaborn
    
    Parámetros:
    n (int): Número de niveles del triángulo (predeterminado: 11)
    paleta (str): Nombre de la paleta de colores de seaborn (predeterminado: 'YlOrBr')
    save_file (str): Ruta para guardar la imagen (predeterminado: None)
    
    Retorna:
    plt: Objeto de matplotlib con la visualización
    """
    df = preparar_datos_triangulo(n)  
    
    # Configuración del estilo
    sns.set_style("darkgrid")
    plt.figure(figsize=(14, 12))
    palette = sns.color_palette(paleta, as_cmap=True)
    max_log_valor = df['log_valor'].max()
    
    # Configuro el eje
    ax = plt.gca()
    ax.set_aspect('equal')
    
    # Creo los triángulos
    for _, row in df.iterrows():
        i, j, valor, orientacion = row['fila'], row['columna'], row['valor'], row['orientacion']
        y = n - i
        x = j + 0.5
        size = 1.0
        
        # Defino la forma del triángulo según la orientación
        if orientacion == 0:  # Triángulo hacia arriba
            triangle = patches.Polygon([
                (x, y),
                (x + size, y - size), 
                (x - size, y - size)
            ], closed=True)
        else:  # Triángulo hacia abajo
            triangle = patches.Polygon([
                (x, y - size), 
                (x + size, y), 
                (x - size, y)
            ], closed=True)
        
        # Asigno color según el valor
        color_intensity = row['log_valor'] / max_log_valor
        triangle.set_facecolor(palette(color_intensity))
        triangle.set_edgecolor('black')
        triangle.set_linewidth(0.5)
        
        # Añado el triángulo al gráfico
        ax.add_patch(triangle)
        
        # Añado el texto con el valor
        text_y = y - 0.5 if orientacion == 0 else y - 0.5
        fontsize = max(6, 14 - n/4)  # Ajusto tamaño de fuente según n
        text_color = 'white' if color_intensity > 0.6 else 'black'
        
        ax.text(x, text_y, str(valor), 
                ha='center', va='center', 
                fontsize=fontsize, 
                color=text_color,
                fontweight='bold')
    
    # Ajusto los límites del gráfico
    plt.xlim(0, 2*n)
    plt.ylim(0, n+1)
    plt.axis('off')  # Oculto los ejes

    # Añado título y leyenda
    plt.title('Triángulo de Pascal', fontsize=24, fontweight='bold', pad=20)
    plt.figtext(0.5, 0.01, f"Niveles: {n} - Cada número es la suma de los dos números de arriba", 
                ha='center', fontsize=12, fontstyle='italic')
    
    # Añado barra de colores
    sm = plt.cm.ScalarMappable(cmap=palette)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', fraction=0.05, pad=0.05)
    cbar.set_label('Magnitud del valor (escala logarítmica)', fontsize=12)
    
    # Guardo la imagen si se especifica
    if save_file:
        try:
            plt.savefig(save_file, dpi=300, bbox_inches='tight')
            print(f"✅ Imagen guardada como '{save_file}'")
        except Exception as e:
            print(f"❌ Error al guardar la imagen: {e}")
    
    plt.tight_layout()
    return plt

def mostrar_propiedades_triangulo(n=11):
    """
    Muestra varias propiedades matemáticas del triángulo de Pascal
    
    Parámetros:
    n (int): Número de niveles del triángulo (predeterminado: 11)
    """
    triangulo = crear_triangulo_pascal(n)
    
    print("\n🔍 PROPIEDADES DEL TRIÁNGULO DE PASCAL")
    print("=" * 50)
    
    # Propiedad 1: Suma de filas (2^n)
    print("\n1️⃣ SUMA DE FILAS = 2^n")
    print("-" * 50)
    for i, fila in enumerate(triangulo):
        suma = sum(fila)
        esperado = 2**i
        print(f"Fila {i}: {' + '.join(map(str, fila))} = {suma} = 2^{i}")
        if suma != esperado:
            print(f"   ❌ Error: La suma debería ser {esperado}")
    
    # Propiedad 2: Números binomiales
    print("\n2️⃣ COEFICIENTES BINOMIALES")
    print("-" * 50)
    print("El valor en la fila n, posición k es el coeficiente binomial C(n,k)")
    for i in range(min(5, n)):  # Mostrar solo hasta 5 filas para no saturar
        for j, valor in enumerate(triangulo[i]):
            print(f"C({i},{j}) = {valor}")
    
    # Propiedad 3: Simetría
    print("\n3️⃣ SIMETRÍA")
    print("-" * 50)
    for i, fila in enumerate(triangulo):
        if len(fila) > 1:  # Solo filas con más de un elemento
            mitad = len(fila) // 2
            es_simetrica = fila[:mitad] == fila[-1:-mitad-1:-1]
            print(f"Fila {i}: {fila}")
            print(f"   {'✅ Simétrica' if es_simetrica else '❌ No simétrica'}")
    
    # Propiedad 4: Secuencias específicas
    print("\n4️⃣ SECUENCIAS ESPECÍFICAS")
    print("-" * 50)
    
    # Números naturales (primera diagonal)
    naturales = [triangulo[i][1] for i in range(1, min(n, 10))]
    print(f"Números naturales (primera diagonal): {naturales}")
    
    # Números triangulares (segunda diagonal)
    triangulares = [triangulo[i][2] for i in range(2, min(n, 10))]
    print(f"Números triangulares (segunda diagonal): {triangulares}")
    
    # Números tetraédricos (tercera diagonal)
    tetraedricos = [triangulo[i][3] for i in range(3, min(n, 10))]
    print(f"Números tetraédricos (tercera diagonal): {tetraedricos}")
    
    # Propiedad 5: Relación con el teorema del binomio
    print("\n5️⃣ TEOREMA DEL BINOMIO")
    print("-" * 50)
    print("El triángulo de Pascal da los coeficientes para (a + b)^n")
    
    n_ejemplo = min(5, n-1)  # Usar un ejemplo manejable
    a, b = 2, 1  # Valores para demostrar (a + b)^n
    resultado = sum(triangulo[n_ejemplo][k] * (a**(n_ejemplo-k)) * (b**k) for k in range(n_ejemplo+1))
    esperado = (a + b)**n_ejemplo
    
    print(f"Para (a + b)^n con a={a}, b={b}, n={n_ejemplo}:")
    terminos = [f"{triangulo[n_ejemplo][k]} × {a}^{n_ejemplo-k} × {b}^{k}" for k in range(n_ejemplo+1)]
    print(f"({a} + {b})^{n_ejemplo} = {' + '.join(terminos)} = {resultado}")
    print(f"Directamente: ({a} + {b})^{n_ejemplo} = {esperado}")
    print(f"   {'✅ Coinciden' if resultado == esperado else '❌ No coinciden'}")

def main():
    """
    Función principal para interactuar con el usuario y visualizar el triángulo de Pascal
    """
    print("\n🔷 TRIÁNGULO DE PASCAL - VISUALIZACIÓN Y PROPIEDADES")
    print("=" * 60)
    print("\nEste programa genera y visualiza el triángulo de Pascal,")
    print("mostrando sus propiedades matemáticas y creando una representación gráfica.")
    
    # Solicitar el número de niveles
    try:
        entrada = input("\n📝 Número de niveles del triángulo [predeterminado=11]: ").strip()
        n = int(entrada) if entrada else 11
        
        if n <= 0:
            print("❌ Error: El número de niveles debe ser positivo.")
            return None
        elif n > 20:
            confirmacion = input(f"⚠️ Advertencia: Un valor de n={n} puede generar números muy grandes y consumir recursos. ¿Continuar? (s/n): ").strip().lower()
            if confirmacion not in ['s', 'si', 'sí', 'y', 'yes']:
                print("🔄 Operación cancelada.")
                return None
        
        # Opciones para la visualización
        print("\n📊 OPCIONES DE VISUALIZACIÓN:")
        print("1. Ver propiedades matemáticas")
        print("2. Generar visualización gráfica")
        print("3. Ambas opciones")
        
        opcion = input("\n➤ Seleccione una opción [predeterminado=3]: ").strip()
        opcion = int(opcion) if opcion else 3
        
        if opcion in [1, 3]:
            mostrar_propiedades_triangulo(n)
        
        if opcion in [2, 3]:
            # Seleccionar paleta de colores
            print("\n🎨 PALETAS DE COLORES DISPONIBLES:")
            paletas = ['YlOrBr', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'Reds', 'Greens', 'Purples']
            for i, paleta in enumerate(paletas, 1):
                print(f"{i}. {paleta}")
            
            entrada = input("\n➤ Seleccione una paleta [predeterminado=1]: ").strip()
            indice_paleta = int(entrada) - 1 if entrada else 0
            
            if indice_paleta < 0 or indice_paleta >= len(paletas):
                indice_paleta = 0  # Valor predeterminado si está fuera de rango
            
            paleta = paletas[indice_paleta]
            
            # Preguntar si desea guardar la imagen
            guardar = input("\n💾 ¿Desea guardar la imagen? (s/n) [predeterminado=s]: ").strip().lower()
            guardar = guardar if guardar else 's'
            
            if guardar in ['s', 'si', 'sí', 'y', 'yes']:
                nombre_archivo = input("➤ Nombre del archivo [predeterminado='triangulo_pascal.png']: ").strip()
                nombre_archivo = nombre_archivo if nombre_archivo else 'triangulo_pascal.png'
                if not nombre_archivo.endswith(('.png', '.jpg', '.jpeg', '.pdf')):
                    nombre_archivo += '.png'
            else:
                nombre_archivo = None
            
            print("\n🔄 Generando visualización...")
            plt = visualizar_triangulo_seaborn(n, paleta, nombre_archivo)
            print("✅ Visualización generada correctamente.")
            
            if nombre_archivo:
                print(f"📄 Imagen guardada como '{nombre_archivo}'")
            else:
                print("ℹ️  No se guardó ninguna imagen.")
            
            plt.close()  # Cerrar la figura para liberar memoria
        
        print("\n✅ Proceso completado exitosamente.")
        return True
        
    except ValueError as e:
        print(f"❌ Error: Valor no válido. {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        return None

# Para uso directo como un script independiente
if __name__ == "__main__":
    main()