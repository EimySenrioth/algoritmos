#liberias usadas
#lo utilizo para el algoritmo np
#pd para manipulacion de datos
#plt para graficar
#sns para graficar oara daler un formamo bonito
#patches para crear figuras geometricas que lo que quermos son triangulo o figuras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Usa un backend sin GUI


import matplotlib.patches as patches


def crear_triangulo_pascal(n):
# creo una lista vacia, e itero en i en un rnago n para cada casilla
#inicio en la fila uno e itero en j en un rango i
#accedo a las filas inferiores en 1-1, y se suman los elementos
# consecutivos en resultado y se suma resultado en 1-1, en j para obtener el valor 
# acrtual y las añado
    resultado = []
    for i in range(n):
        fila = [1]
        for j in range(1, i):
            fila.append(resultado[i-1][j-1] + resultado[i-1][j])
        if i > 0:
            fila.append(1)
        resultado.append(fila)
    return resultado

def preparar_datos_triangulo(n):
 
    triangulo = crear_triangulo_pascal(n=11)
#paso a una nueva varieble
#creo listas vacias, para filas del triangulo, columnas, valores del triangulo
#orientaciones
# 0 para triángulo hacia arriba, 1 para triángulo hacia abajo eb valores
    filas = []
    columnas = []
    valores = []
    orientaciones = []  
#se recorre cada fila en i es el idice y fila es la lista
#dentro de cada fila se recorre j que es el indice valor y valor es la posicion
    
    for i, fila in enumerate(triangulo):
        for j, valor in enumerate(fila):
#aqui se ajusta la pociion
#n-1-i-1 es la posicion de la fila en la matriz
#j*2 es la posicion de la columna en la matriz 
            col_pos = n - i - 1 + j * 2  
            
# Agregar datosm en orientaciones lo alterno entro 0 y 1
#para que se vea el triangulo hacia arriba y hacia abajo
            filas.append(i)
            columnas.append(col_pos)
            valores.append(valor)
            orientaciones.append(j % 2)  
            
# Creo un dataframw
#dila son los indece de la fila
#valor nimero del triangulo de pascal
#orientacion del triagulo 1 y 0
#logitmo para contiene el logaritmo natural de (valor + 1) para cada fila.
#Cuando los datos tienen valores muy grandes o muy dispersos
#Agregar una nueva columna log_valor al DataFrame df.
#em otras palabras Preparar datos para análisis o visualización
    df = pd.DataFrame({
        'fila': filas,
        'columna': columnas,
        'valor': valores,
        'orientacion': orientaciones,
        'log_valor': np.log1p(valores) 
    
    })
    
    return df
#creo la funcion poniendo la n una paleta y valor indetermidado para guardar
#uso estilo grafico en seaborn con pulgadas
#pongo una pleta de colores
def visualizar_triangulo_seaborn(n, paleta='YlOrBr', save_file=None):
    df = preparar_datos_triangulo(n)  
    sns.set_style("darkgrid")
    plt.figure(figsize=(14, 12))
    palette = sns.color_palette(paleta, as_cmap=True)
    max_log_valor = df['log_valor'].max()
#normalizo los colores con el max
    ax = plt.gca()
#ontengo el ejeje acutao y se ajusta
    ax.set_aspect('equal')
# se recorre cada fila de dtaframe, el row contiene los datos de una fila
#i es el inde, j la columna indice, valor nimero del triangulo, orientacion del triagulo
#y es la posicion vertical para que las filas superiores este arriba, mas
#la posicion horizontal para centrar los triangulo
#size es el tamaño del triangulo
    for _, row in df.iterrows():
        i, j, valor, orientacion = row['fila'], row['columna'], row['valor'], row['orientacion']
        y = n - i
        x = j + 0.5
        size = 1.0
# Triángulo hacia arriba
#esta parte creo los tenigulos individuealesm xy son las cornedas
        if orientacion == 0:  
            triangle = patches.Polygon([
                (x, y), #es el vertice superior y el siguiente el inferio derecho e izquierdo
                (x + size, y - size), 
                (x - size, y - size)
            ], closed=True)
# Triángulo hacia abajo y es el inferior y el closed true es para que se cierre
        else:  
            triangle = patches.Polygon([
                (x, y - size), 
                (x + size, y), 
                (x - size, y)
            ], closed=True)
        
# Color basado en el valor normalizado
#calculo la intencidad dividiendo el algoritmo del triangulo actual por el valor
#maximo esto normaliza los valores 0-1, agrego color
#borde negro, pongo un grosoe
        color_intensity = row['log_valor'] / max_log_valor
        triangle.set_facecolor(palette(color_intensity))
        triangle.set_edgecolor('black')
        triangle.set_linewidth(0.5)
        
# Añadir el triángulo al gráfico, nuermo, fuente y color orientacion
#en text... colcilo pa posicion vertical conde se colo el texto
#usadon == el textose coloca debajo del vertice superio y ocurre lo conrario
#ajute del neto dinamico, es decir a medida que n aumenta el tamaño disminuye
#se elife el tecxto con dos opciones con una intencidad dependiendo
#añado el texto al grafico, con cornedadas xy, usadondo una strin del valor
#loa ha, va alienan el texto horizotal y verticalmente en el centro del triangulo
#le pongro que el texto sea mas gureso
        ax.add_patch(triangle)
        text_y = y - 0.5 if orientacion == 0 else y - 0.5
        fontsize = max(6, 14 - n/4)
        text_color = 'white' if color_intensity > 0.6 else 'black'
        
        ax.text(x, text_y, str(valor), 
                ha='center', va='center', 
                fontsize=fontsize, 
                color=text_color,
                fontweight='bold')
    
# Ajustar los límites en eje le orizaonta en x para que abarque el doble de nuebero de n del tringulo
#y el eje vertical en y para que abarque el numero de filas, 
    plt.xlim(0, 2*n)
    plt.ylim(0, n+1)
#oculto los ejes del grafico
    plt.axis('off')

    plt.title('Triángulo de Pascal', fontsize=24, fontweight='bold', pad=20)
    
    plt.figtext(0.5, 0.01, f"Niveles: {n} - Cada número es la suma de los dos números de arriba", 
                ha='center', fontsize=12, fontstyle='italic')
    
#aqui creo un objeto para mapear los colores a segun la paleta en sm
#alado una barra de colores, e horizontal, el tamaño y espacio
#añado etiquetas
    sm = plt.cm.ScalarMappable(cmap=palette)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', fraction=0.05, pad=0.05)
    cbar.set_label('Magnitud del valor (escala logarítmica)', fontsize=12)
    

    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches='tight')
    
    plt.tight_layout()
    return plt


n = 11
plt = visualizar_triangulo_seaborn(n, paleta='YlOrBr', save_file='triangulo_pascal_seaborn.png')


