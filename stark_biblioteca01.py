##Funcion stark_normalizar_datos (list:lista): -> none
##Se encarga validar primero que el tipo de dato no sea del tipo al cual será casteado.
def stark_normalizar_datos(lista):
    if len(lista) == 0:
        print("Error: Lista de héroes vacía")
        return

    tipos_numericos = (int, float)

    datos_modificados = False

    for heroe in lista:
        for key, value in heroe.items():
            if isinstance(value, str):
                # Verificar si se puede convertir a int
                if key in ["fuerza"]:
                    try:
                        int_value = int(value)
                        heroe[key] = int_value
                        datos_modificados = True
                    except ValueError:
                        pass  # No se puede convertir a int
                # Verificar si se puede convertir a float
                elif key in ["altura", "peso"]:
                    try:
                        float_value = float(value)
                        heroe[key] = float_value
                        datos_modificados = True
                    except ValueError:
                        pass  # No se puede convertir a float

    if datos_modificados:
        print("Datos normalizados")

def obtener_nombre(heroe):
    nombre = heroe.get('nombre', '')
    nombre_formateado = f"Nombre: {nombre}"
    return nombre_formateado


def imprimir_dato(dato):
    print(dato)

def stark_imprimir_nombres_heroes(lista):
    if len(lista) == 0:
        return -1

    for heroe in lista:
        nombre_formateado = obtener_nombre(heroe)
        imprimir_dato(nombre_formateado)

    return None


def obtener_nombre_y_dato(heroe, key):
    nombre = obtener_nombre(heroe)
    dato = heroe.get(key, '')

    nombre_y_dato = f"{nombre} | {key}: {dato}"
    return nombre_y_dato

def stark_imprimir_nombres_alturas(lista):
    if len(lista) == 0:
        return -1

    for heroe in lista:
        altura = float(heroe.get('altura', 0))
        nombre_altura = obtener_nombre_y_dato(heroe, f'altura: {altura}')
        imprimir_dato(nombre_altura)

    return None

def calcular_max(lista, key):
    if len(lista) == 0:
        return None

    max_valor = float('-inf')
    heroe_max = None

    for heroe in lista:
        valor = float(heroe.get(key, 0))
        if valor > max_valor:
            max_valor = valor
            heroe_max = heroe

    return heroe_max

def calcular_min(lista, key):
    if len(lista) == 0:
        return None

    min_valor = float('inf')
    heroe_min = None

    for heroe in lista:
        if key in heroe:
            valor = float(heroe.get(key, 0))
        
            if valor < min_valor:
                min_valor = valor
                heroe_min = heroe

    return heroe_min

def calcular_max_min_dato(lista, tipo_calculo, key):
    if tipo_calculo == 'maximo':
        return calcular_max(lista, key)
    elif tipo_calculo == 'minimo':
        return calcular_min(lista, key)
    else:
        return None


def stark_calcular_imprimir_heroe(lista, tipo_calculo, key):
    heroe_resultado = calcular_max_min_dato(lista, tipo_calculo, key)

    if heroe_resultado is None:
        return

    nombre_dato = obtener_nombre_y_dato(heroe_resultado, key)
    imprimir_dato(f"{tipo_calculo} {key} {nombre_dato}")

def sumar_dato_heroe(lista, key):
    suma = 0
    
    for heroe in lista:
        if isinstance(heroe, dict) and heroe:
            if key in heroe:
                valor = heroe[key]
                try:
                    suma += float(valor)
                except ValueError:
                    print(f"El valor '{valor}' para la clave '{key}' no es un número válido.")
    
    return suma

def dividir(dividendo, divisor):
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor

def calcular_promedio(lista, key):
    total = sumar_dato_heroe(lista, key)
    cantidad_heroes = len(lista)

    if cantidad_heroes == 0:
        return 0
    else:
        return dividir(total, cantidad_heroes)

def stark_calcular_imprimir_promedio_altura(lista):
    if len(lista) == 0:
        return -1

    promedio_altura = calcular_promedio(lista, 'altura')
    imprimir_dato(f"Promedio de altura: {promedio_altura}")
    
def imprimir_menu():
    menu2 = """
    -------- Menú ---------
    1. Obtener nombre de héroe
    2. Imprimir lista de héroes
    3. Calcular máximo o mínimo (peso, altura)
    4. Calcular y mostrar promedio de altura
    5. Salir
    """
    print (menu2)

def validar_entero(numero):
    if numero.isdigit():
        return True
    else:
        return False

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese el número de la opción elegida: ")
    
    if validar_entero(opcion):
        return int(opcion)
    else:
        return -1
    

def stark_marvel_app(lista_heroes):
    import os
    while True:
        opcion = stark_menu_principal()
        
        if opcion == 1:
            stark_imprimir_nombres_heroes(lista_heroes)
        elif opcion == 2:
            stark_imprimir_nombres_alturas(lista_heroes)
        elif opcion == 3:
            dato1 = input("Desea maximo o minimo: ")
            dato2 = input("Dato a obtener (peso o altura): ")
            stark_calcular_imprimir_heroe(lista_heroes, dato1, dato2)
        elif opcion == 4:
            stark_calcular_imprimir_promedio_altura(lista_heroes)
        elif opcion == 5:
            break
        else:
            print("Opción incorrecta. Por favor, seleccione una opción válida.")
        os.system("pause")
        os.system("cls")