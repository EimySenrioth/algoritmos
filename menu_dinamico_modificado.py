import os
import sys
import importlib.util
import inspect

class MenuDinamico:
    def __init__(self, directorios_busqueda=None):
        if directorios_busqueda is None:
            directorios_busqueda = [".", "app/backend", "algoritmos", "src"]
        
        self.directorios = directorios_busqueda
        self.algoritmos = {}
        self.archivo_a_id = {}  # Mapeo de nombres de archivo a IDs
        self.archivos_disponibles = []  # Lista de archivos disponibles pero no cargados

    def buscar_archivos_python(self):
        """Busca archivos .py en los directorios especificados pero no los carga"""
        archivos_encontrados = []
        
        for directorio in self.directorios:
            if os.path.exists(directorio):
                print(f"🔍 Buscando en directorio: {directorio}")
                for archivo in os.listdir(directorio):
                    if archivo.endswith('.py') and not archivo.startswith('__') and archivo not in ['menu_dinamico.py', 'menu_dinamico_mejorado.py']:
                        ruta_completa = os.path.join(directorio, archivo)
                        archivos_encontrados.append((archivo, ruta_completa, directorio))
                        print(f"  ✅ Encontrado: {archivo}")
        
        return archivos_encontrados
    
    def indexar_archivos_disponibles(self):
        """Indexa los archivos disponibles sin cargarlos"""
        archivos_py = self.buscar_archivos_python()
        
        if not archivos_py:
            print("❌ No se encontraron archivos de algoritmos")
            return
        
        contador = 1
        print(f"\n📋 ALGORITMOS DISPONIBLES:")
        print("-" * 60)
        
        for archivo, ruta_completa, directorio in archivos_py:
            nombre_modulo = archivo[:-3]  # Quitar .py
            self.archivos_disponibles.append({
                'id': contador,
                'nombre': nombre_modulo.replace('_', ' ').title(),
                'archivo': archivo,
                'ruta_completa': ruta_completa,
                'directorio': directorio
            })
            print(f"  [{contador:2d}] {archivo}")
            contador += 1
            
        return True

    def cargar_algoritmo_especifico(self, id_algoritmo):
        """Carga solo un algoritmo específico según su ID"""
        if id_algoritmo < 1 or id_algoritmo > len(self.archivos_disponibles):
            print(f"❌ ID de algoritmo inválido: {id_algoritmo}")
            return False
            
        info_archivo = self.archivos_disponibles[id_algoritmo - 1]
        archivo = info_archivo['archivo']
        ruta_completa = info_archivo['ruta_completa']
        directorio = info_archivo['directorio']
        
        print(f"\n📦 CARGANDO ALGORITMO: {archivo}")
        print("-" * 60)
        
        try:
            nombre_modulo = archivo[:-3]  # Quitar .py
            
            # Cargar el módulo dinámicamente
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_completa)
            modulo = importlib.util.module_from_spec(spec)
            
            # Agregar el directorio al path temporalmente
            if directorio not in sys.path:
                sys.path.insert(0, directorio)
            
            try:
                spec.loader.exec_module(modulo)
            except Exception as e:
                print(f"❌ Error al ejecutar módulo {archivo}: {e}")
                return False
            
            # Buscar funciones principales
            funciones_candidatas = []
            
            # Buscar funciones que no empiecen con _
            for nombre_func, obj in inspect.getmembers(modulo):
                if inspect.isfunction(obj) and not nombre_func.startswith('_'):
                    funciones_candidatas.append(nombre_func)
            
            if not funciones_candidatas:
                print(f"⚠️  No se encontraron funciones ejecutables en {archivo}")
                return False
            
            # Determinar la función principal con estrategias mejoradas
            funcion_principal = None
            nombre_funcion = None
            
            # Estrategia 1: Buscar función 'main'
            if "main" in funciones_candidatas:
                funcion_principal = getattr(modulo, "main")
                nombre_funcion = "main"
            
            # Estrategia 2: Para archivos específicos, buscar funciones conocidas
            elif nombre_modulo == "rpm" and "rpm" in funciones_candidatas:
                funcion_principal = getattr(modulo, "rpm")
                nombre_funcion = "rpm"
            elif nombre_modulo == "rpm_binari" and "rpm_binari" in funciones_candidatas:
                funcion_principal = getattr(modulo, "rpm_binari")
                nombre_funcion = "rpm_binari"
            elif nombre_modulo == "newtonraiz" and "newton_raiz" in funciones_candidatas:
                funcion_principal = getattr(modulo, "newton_raiz")
                nombre_funcion = "newton_raiz"
            elif nombre_modulo == "prime_factorization" and "factorize" in funciones_candidatas:
                funcion_principal = getattr(modulo, "factorize")
                nombre_funcion = "factorize"
            elif nombre_modulo == "maximo_comun_divisor" and "mcd" in funciones_candidatas:
                funcion_principal = getattr(modulo, "mcd")
                nombre_funcion = "mcd"
            
            # Estrategia 3: Buscar función que coincida con el nombre del archivo
            elif funcion_principal is None:
                for func_name in funciones_candidatas:
                    if func_name == nombre_modulo or nombre_modulo in func_name:
                        funcion_principal = getattr(modulo, func_name)
                        nombre_funcion = func_name
                        break
            
            # Estrategia 4: Si no encuentra coincidencia, tomar la primera función
            if funcion_principal is None:
                nombre_funcion = funciones_candidatas[0]
                funcion_principal = getattr(modulo, nombre_funcion)
            
            # Determinar el nombre descriptivo
            nombre_descriptivo = nombre_modulo.replace('_', ' ').title()
            
            # Mapeo personalizado para nombres más descriptivos
            nombres_descriptivos = {
                "rpm": "Russian Peasant Multiplication (RPM)",
                "borrowing": "Algoritmo de préstamo/borrowing",
                "carrying": "Algoritmo de acarreo/carrying",
                "complementation": "Complementación de números",
                "cortepasteles": "Problema de corte de pasteles",
                "exponentiation": "Exponenciación rápida",
                "itriangle": "Triángulo de números (iTriangle)",
                "maximo_comun_divisor": "Máximo Común Divisor (MCD)",
                "newtonraiz": "Método de Newton para raíces",
                "prime_factoritation": "Factorización en números primos",
                "prime_tester": "Verificador de números primos",
                "rpm_binari": "RPM en implementación binaria",
                "rpmi": "Russian Peasant Multiplication Implementation",
                "base_2_8_16": "Conversiones base 2, 8 y 16",
                "ecluide": "Algoritmo de Euclides",
                "error_a_r": "Errores absoluto y relativo",
                "nbiseecction": "Método de bisección numérica",
                "prime_tester_1": "Tester de primos versión 1",
                "prime_tester3": "Tester de primos versión 3",
                "principiopalomar": "Principio del Palomar",
                "casting_out_nines": "Casting Out Nines",
                "unificado_primes": "Primos Unificado"
            }
            
            # Buscar coincidencia exacta primero
            nombre_base = nombre_modulo.lower()
            if nombre_base in nombres_descriptivos:
                nombre_descriptivo = nombres_descriptivos[nombre_base]
            else:
                # Buscar coincidencia parcial
                for clave, descripcion in nombres_descriptivos.items():
                    if clave in nombre_base or nombre_base in clave:
                        nombre_descriptivo = descripcion
                        break
            
            # Guardar el algoritmo en el diccionario
            self.algoritmos[1] = {
                'nombre': nombre_descriptivo,
                'funcion': funcion_principal,
                'archivo': archivo,
                'directorio': directorio,
                'nombre_funcion': nombre_funcion,
                'ruta_completa': ruta_completa,
                'modulo': modulo
            }
            
            # También guardar una versión sin extensión .py
            self.archivo_a_id[archivo.lower()] = 1
            self.archivo_a_id[nombre_modulo.lower()] = 1
            
            print(f"✅ Algoritmo cargado: {nombre_descriptivo}")
            print(f"     📁 {archivo} | ⚙️ {nombre_funcion} | 📍 {directorio}")
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar {archivo}: {e}")
            import traceback
            traceback.print_exc()
            return False

    def mostrar_menu(self):
        print("\n" + "🟦" * 40)
        print(" " * 12 + "MENÚ DE ALGORITMOS MATEMÁTICOS")
        print("🟦" * 40)
        
        if not self.algoritmos:
            print("❌ No se encontraron algoritmos en los directorios especificados")
            print("📁 Directorios buscados:", ", ".join(self.directorios))
            return
        
        # Mostrar lista numerada con formato claro
        print(f"\n📚 ALGORITMOS DISPONIBLES ({len(self.algoritmos)} encontrados):")
        print("═" * 80)
        
        for num in sorted(self.algoritmos.keys()):
            info = self.algoritmos[num]
            
            # Emoji por categoría
            nombre = info['nombre'].lower()
            if any(x in nombre for x in ['prime', 'factor', 'gcd', 'mcd', 'rpm', 'multiplication']):
                emoji = "🔢"  # Aritmética
            elif any(x in nombre for x in ['newton', 'bisec', 'raiz', 'triangle']):
                emoji = "📐"  # Cálculo
            elif any(x in nombre for x in ['conversion', 'base']):
                emoji = "🔄"  # Conversiones
            else:
                emoji = "⚡"  # Otros
            
            print(f"{emoji} [{num:2d}] {info['nombre']}")
            print(f"      📄 {info['archivo']} | 🔧 {info['nombre_funcion']} | 📁 {info['directorio']}")
            print()
        
        print("═" * 80)
        print("🚪 [0] Salir del programa")
        print("═" * 80)

    def confirmar_seleccion(self, opcion):
        """Confirma la selección del usuario"""
        if opcion in self.algoritmos:
            info = self.algoritmos[opcion]
            print(f"\n📋 Has seleccionado:")
            print(f"   🔹 Algoritmo: {info['nombre']}")
            print(f"   🔹 Archivo: {info['archivo']}")
            print(f"   🔹 Función: {info['nombre_funcion']}")
            
            confirmacion = input("\n❓ ¿Confirmas que quieres ejecutar este algoritmo? (s/n): ").strip().lower()
            return confirmacion in ['s', 'si', 'sí', 'y', 'yes']
        return False

    def ejecutar_opcion(self, opcion):
        if opcion == 0:
            print("\n👋 ¡Gracias por usar el programa!")
            return False
        elif opcion in self.algoritmos:
            # Confirmar selección
            if not self.confirmar_seleccion(opcion):
                print("❌ Ejecución cancelada")
                return True
            
            info = self.algoritmos[opcion]
            print(f"\n{'🟨' * 30}")
            print(f"  EJECUTANDO: {info['nombre']}")
            print(f"{'🟨' * 30}")
            print(f"📁 Archivo: {info['ruta_completa']}")
            print(f"⚙️  Función: {info['nombre_funcion']}")
            print(f"📍 Directorio: {info['directorio']}")
            print("─" * 70)
            
            try:
                # Verificar si la función acepta parámetros
                sig = inspect.signature(info['funcion'])
                params = list(sig.parameters.keys())
                
                if not params:
                    # Función sin parámetros
                    resultado = info['funcion']()
                else:
                    # Mostrar los parámetros requeridos
                    print(f"ℹ️  La función requiere parámetros: {params}")
                    print("❓ ¿Desea ejecutar la función con los parámetros predeterminados? (s/n): ", end="")
                    respuesta = input().strip().lower()
                    
                    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                        try:
                            resultado = info['funcion']()
                            print("✅ Función ejecutada con valores predeterminados")
                        except TypeError as e:
                            print(f"❌ Error: {e}")
                            print("ℹ️  Esta función requiere parámetros específicos.")
                            print("🔍 Volviendo al menú principal...")
                            return True
                    else:
                        print("🔍 Volviendo al menú principal...")
                        return True
                
                # Si la función retorna algo, mostrarlo
                if resultado is not None:
                    print(f"\n✅ Resultado: {resultado}")
                else:
                    print("\n✅ Algoritmo ejecutado con éxito")
                    
            except Exception as e:
                print(f"\n❌ Error al ejecutar el algoritmo: {e}")
                print("\n🔍 Información adicional del error:")
                import traceback
                traceback.print_exc()
            
            print("─" * 70)
            input("\n⏸️  Presione Enter para volver al menú...")
            return True
        else:
            print(f"❌ Opción inválida. Elija un número entre 0 y {len(self.algoritmos)}")
            return True

    def buscar_por_nombre(self, texto_busqueda):
        """Busca algoritmos por nombre de archivo"""
        texto_busqueda = texto_busqueda.lower()
        
        # Verificar coincidencia exacta primero
        if texto_busqueda in self.archivo_a_id:
            return self.archivo_a_id[texto_busqueda]
            
        # Si no hay coincidencia exacta, buscar coincidencias parciales
        coincidencias = []
        
        # Buscar en nombres de archivo
        for archivo, id_algoritmo in self.archivo_a_id.items():
            if texto_busqueda in archivo:
                coincidencias.append((id_algoritmo, self.algoritmos[id_algoritmo]['archivo']))
        
        # Buscar en nombres descriptivos
        for id_algoritmo, info in self.algoritmos.items():
            if texto_busqueda in info['nombre'].lower():
                # Verificar que no esté ya en coincidencias
                if not any(id_algoritmo == id_alg for id_alg, _ in coincidencias):
                    coincidencias.append((id_algoritmo, info['archivo']))
        
        if not coincidencias:
            return None
        elif len(coincidencias) == 1:
            return coincidencias[0][0]  # Devolver el ID si solo hay una coincidencia
        else:
            # Mostrar las opciones encontradas
            print(f"\n🔍 Se encontraron {len(coincidencias)} coincidencias para '{texto_busqueda}':")
            for i, (id_alg, archivo) in enumerate(coincidencias, 1):
                print(f"  {i}. [{id_alg}] {self.algoritmos[id_alg]['nombre']} ({archivo})")
            
            # Pedir al usuario que elija
            while True:
                try:
                    seleccion = input("\n➤ Seleccione una opción (número): ").strip()
                    
                    # Verificar si ingresó un índice de la lista
                    if seleccion.isdigit() and 1 <= int(seleccion) <= len(coincidencias):
                        return coincidencias[int(seleccion) - 1][0]
                    # O si ingresó el ID directamente
                    elif seleccion.isdigit() and int(seleccion) in self.algoritmos:
                        return int(seleccion)
                    else:
                        print("❌ Selección inválida, intente de nuevo")
                except ValueError:
                    print("❌ Por favor ingrese un número válido")
            
        return None

    def obtener_entrada_usuario(self):
        """Obtiene y valida la entrada del usuario"""
        print(f"\n🎯 Elija una opción:")
        print(f"   📌 Ingrese un número (1-{len(self.algoritmos)}) o el nombre del archivo")
        print(f"   📌 Ingrese '0' para salir")
        
        entrada = input("\n➤ Su elección: ").strip()
        
        # Verificar si es un número
        if entrada.isdigit():
            opcion = int(entrada)
            # Verificar rango válido
            if 0 <= opcion <= len(self.algoritmos):
                return opcion
            else:
                print(f"❌ Número fuera de rango. Use números entre 0 y {len(self.algoritmos)}")
                return None
        # Si no es un número, buscar por nombre
        elif entrada:
            opcion = self.buscar_por_nombre(entrada)
            if opcion is not None:
                return opcion
            else:
                print(f"❌ No se encontró ningún algoritmo que coincida con '{entrada}'")
                return None
        else:
            print("❌ Entrada vacía, por favor ingrese una opción válida")
            return None

    def ejecutar(self):
        """Método principal que ejecuta el menú selectivo"""
        # Indexar primero los archivos disponibles
        if not self.indexar_archivos_disponibles():
            print("❌ No se encontraron algoritmos para ejecutar")
            print("📁 Verifique que los archivos estén en los directorios correctos:")
            for directorio in self.directorios:
                existe = "✅" if os.path.exists(directorio) else "❌"
                print(f"  {existe} {directorio}")
            return
        
        print("\n📝 Seleccione el algoritmo que desea ejecutar:")
        print("   📌 Ingrese el número del algoritmo (1-{})".format(len(self.archivos_disponibles)))
        print("   📌 Ingrese '0' para salir")
        
        continuar = True
        while continuar:
            try:
                seleccion = input("\n➤ Su elección: ").strip()
                
                if seleccion == '0':
                    print("\n👋 ¡Gracias por usar el programa!")
                    break
                
                if seleccion.isdigit():
                    id_algoritmo = int(seleccion)
                    if 1 <= id_algoritmo <= len(self.archivos_disponibles):
                        # Limpiar algoritmos previos
                        self.algoritmos = {}
                        self.archivo_a_id = {}
                        
                        # Cargar solo el algoritmo seleccionado
                        if self.cargar_algoritmo_especifico(id_algoritmo):
                            # Ejecutar el algoritmo
                            self.ejecutar_opcion(1)  # Siempre será 1 porque solo hay un algoritmo cargado
                        else:
                            print("❌ Error al cargar el algoritmo seleccionado")
                    else:
                        print(f"❌ Número fuera de rango. Elija entre 1 y {len(self.archivos_disponibles)}")
                else:
                    print("❌ Por favor ingrese un número válido")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Programa interrumpido por el usuario")
                break

def main():
    print("🚀 INICIANDO MENU DINÁMICO DE ALGORITMOS")
    print("=" * 50)
    print("🔍 Buscando algoritmos en directorios...")
    
    # Directorios donde buscar algoritmos
    directorios_busqueda = [".", "app/backend", "algoritmos", "src", "backend"]
    
    # Permitir al usuario especificar directorios adicionales
    print("\n📁 Directorios de búsqueda configurados:")
    for i, directorio in enumerate(directorios_busqueda, 1):
        existe = "✅" if os.path.exists(directorio) else "❌"
        print(f"  {i}. {directorio} {existe}")
    
    directorio_extra = input("\n📂 ¿Agregar directorio adicional? (Enter para omitir): ").strip()
    if directorio_extra:
        if os.path.exists(directorio_extra):
            directorios_busqueda.insert(0, directorio_extra)
            print(f"✅ Directorio agregado: {directorio_extra}")
        else:
            print(f"❌ Directorio no encontrado: {directorio_extra}")
    
    print("\n🚀 Inicializando menú dinámico...")
    menu = MenuDinamico(directorios_busqueda)
    menu.ejecutar()

if __name__ == "__main__":
    main()
    