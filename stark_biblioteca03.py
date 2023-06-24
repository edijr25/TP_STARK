from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe):
    if not nombre_heroe:
        return 'N/A'

    # Reemplazar guiones por espacios en blanco
    nombre_heroe = nombre_heroe.replace('-', ' ')

    # Dividir el nombre en palabras
    palabras = nombre_heroe.split()

    # Filtrar las palabras que no son el artículo "the"
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() != 'the']

    # Tomar la primera letra de cada palabra y convertirla a mayúscula
    iniciales = [palabra[0].upper() for palabra in palabras_filtradas]

    # Unir las iniciales con puntos y devolver el resultado
    return '.'.join(iniciales) + '.'

def definir_iniciales_nombre(heroe):
    if not isinstance(heroe, dict):
        return False

    if 'nombre' not in heroe:
        return False

    nombre_heroe = heroe['nombre']
    iniciales = extraer_iniciales(nombre_heroe)
    heroe['iniciales'] = iniciales
    return True

def agregar_iniciales_nombre(lista_heroes):
    if not isinstance(lista_heroes, list):
        print('El origen de datos no contiene el formato correcto')
        return False

    if len(lista_heroes) == 0:
        print('El origen de datos no contiene al menos un elemento')
        return False

    for heroe in lista_heroes:
        if not definir_iniciales_nombre(heroe):
            print('El origen de datos no contiene el formato correcto')
            return False

    return True

def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if not isinstance(lista_heroes, list):
        print('El origen de datos no contiene el formato correcto')
        return

    if len(lista_heroes) == 0:
        print('El origen de datos no contiene al menos un elemento')
        return

    if agregar_iniciales_nombre(lista_heroes):
        for heroe in lista_heroes:
            nombre = heroe['nombre']
            iniciales = heroe['iniciales']
            print(f"* {nombre} ({iniciales})")
    else:
        print('Error al agregar las iniciales a los nombres')

def generar_codigo_heroe(genero_heroe, id_heroe):
    if not isinstance(id_heroe, int) or genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'

    codigo = f"{genero_heroe}-" + str(id_heroe).zfill(8)
    return codigo


def agregar_codigo_heroe(heroe, id_heroe):
    if not heroe or not isinstance(heroe, dict):
        return False

    codigo = generar_codigo_heroe(heroe['genero'], id_heroe)  # Corrección aquí
    if codigo == 'N/A':
        return False

    heroe['codigo_heroe'] = codigo
    return True


def stark_generar_codigos_heroes(lista):
    if not lista or not all(isinstance(heroe, dict) for heroe in lista):
        print (lista)
        print("El origen de datos no contiene el formato correcto")
        return

    cantidad_codigos = len(lista)
    contador = 1

    for heroe in lista:
        if agregar_codigo_heroe(heroe, contador):
            print(f"Se generó el código para el héroe: {heroe['nombre']}")
        else:
            print(f"Error al generar el código para el héroe: {heroe['nombre']}")
        contador += 1

    print(f"Se asignaron {cantidad_codigos} códigos")



#stark_generar_codigos_heroes(lista_personajes)

def sanitizar_entero(numero_str):
    numero_str = numero_str.strip()  # Eliminar espacios en blanco al inicio y final

    if not numero_str.isdigit():  # Verificar si contiene caracteres no numéricos
        return -1

    numero = int(numero_str)  # Convertir a entero

    if numero < 0:  
        return -2

    return numero

def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip()  # Eliminar espacios en blanco al inicio y final

    # Verificar si el número es negativo
    if numero_str.startswith('-'):
        return -2

    try:
        numero_float = float(numero_str)
        if numero_float < 0:
            return -2
        else:
            return numero_float
    except ValueError:
        return -1
    except:
        return -3

def sanitizar_string(valor_str, valor_por_defecto='-'):
    valor_str = valor_str.strip()  # Eliminar espacios en blanco al inicio y final
    valor_por_defecto = valor_por_defecto.strip()  # Eliminar espacios en blanco al inicio y final

    # Reemplazar barra '/' por espacio
    valor_str = valor_str.replace('/', ' ')

    # Verificar si el texto contiene números
    if any(char.isdigit() for char in valor_str):
        return "N/A"

    # Convertir el texto a minúsculas si solo contiene letras
    if valor_str.isalpha():
        return valor_str.lower()

    # Verificar si el texto está vacío y se proporcionó un valor por defecto
    if valor_str == '' and valor_por_defecto != '':
        return valor_por_defecto.lower()

    return valor_str.lower()

def sanitizar_dato(heroe, clave, tipo_dato):
    tipo_dato = tipo_dato.lower()  # Convertir tipo_dato a minúsculas

    # Validar tipo_dato
    if tipo_dato not in ['string', 'entero', 'flotante']:
        print('Tipo de dato no reconocido')
        return False

    # Validar clave existente en el diccionario heroe
    if clave not in heroe:
        print('La clave especificada no existe en el héroe')
        return False

    valor = heroe[clave]  # Obtener el valor correspondiente a la clave

    if tipo_dato == 'string':
        heroe[clave] = sanitizar_string(valor)
    elif tipo_dato == 'entero':
        heroe[clave] = sanitizar_entero(valor)
    elif tipo_dato == 'flotante':
        heroe[clave] = sanitizar_flotante(valor)

    return True

def stark_normalizar_datos(lista_heroes):
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "inteligencia", "string")

    print("Datos normalizados")

def generar_indice_nombres(lista_heroes):
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
        return []

    nombres = []

    for heroe in lista_heroes:
        if not isinstance(heroe, dict) or "nombre" not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return []

        nombre = heroe["nombre"]
        palabras = nombre.split()
        nombres.extend(palabras)

    return nombres

def stark_imprimir_indice_nombre(lista_heroes):
    nombres = generar_indice_nombres(lista_heroes)
    if nombres:
        indice = ", ".join(nombres)
        print(indice)
    else:
        print("El índice de nombres no está disponible.")

def convertir_cm_a_mtrs(valor_cm):
    if isinstance(valor_cm, (int, float)) and valor_cm > 0:
        valor_mtrs = valor_cm / 100.0
        return valor_mtrs
    else:
        return -1

def generar_separador(patron, largo, imprimir=True):
    if len(patron) < 1 or len(patron) > 2 or not isinstance(largo, int) or largo < 1 or largo > 235:
        return 'N/A'
    
    separador = patron * largo
    
    if imprimir:
        print(separador)
    
    return separador

def generar_encabezado(titulo):
    separador = generar_separador('*', 80, False)  # Ajusta el largo del separador según tus necesidades
    
    titulo_mayusculas = titulo.upper()
    
    encabezado = f"{separador}\n{titulo_mayusculas}\n{separador}"
    
    return encabezado

def imprimir_ficha_heroe(heroe):
    titulo = 'Principal'
    encabezado = generar_encabezado(titulo)

    nombre = heroe['nombre']
    identidad_secreta = heroe['identidad']
    consultora = heroe['empresa']
    codigo_heroe = heroe['codigo_heroe']

    titulo_fisico = 'Fisico'
    encabezado_fisico = generar_encabezado(titulo_fisico)

    altura_cm = heroe['altura']
    peso = heroe['peso']
    fuerza = heroe['fuerza']

    titulo_senas_particulares = 'Señas Particulares'
    encabezado_senas_particulares = generar_encabezado(titulo_senas_particulares)

    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']

    ficha_heroe = f"{encabezado}\nNOMBRE DEL HÉROE: {nombre}\nIDENTIDAD SECRETA: {identidad_secreta}\nCONSULTORA: {consultora}\nCÓDIGO DE HÉROE: {codigo_heroe}\n{encabezado_fisico}\nALTURA: {convertir_cm_a_mtrs(altura_cm)} Mtrs.\nPESO: {peso} Kg.\nFUERZA: {fuerza} N\n{encabezado_senas_particulares}\nCOLOR DE OJOS: {color_ojos}\nCOLOR DE PELO: {color_pelo}"

    print(ficha_heroe)

def stark_navegar_fichas(lista_heroes):
    total_heroes = len(lista_heroes)
    indice_actual = 0

    while True:
        heroe_actual = lista_heroes[indice_actual]
        imprimir_ficha_heroe(heroe_actual)

        opcion = input("[ 1 ] Ir a la izquierda\n[ 2 ] Ir a la derecha\n[ S ] Salir\n")

        if opcion == '1':
            indice_actual -= 1
            if indice_actual < 0:
                indice_actual = total_heroes - 1
        elif opcion == '2':
            indice_actual += 1
            if indice_actual >= total_heroes:
                indice_actual = 0
        elif opcion.upper() == 'S':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

    print("Volviendo al menú principal.")


def imprimir_menu():
    menu = """
____________________________________________________________
                MENU
                
1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir
____________________________________________________________
"""
    print(menu)

def stark_menu_principal():
    respuesta = input("Ingrese una opción: ")
    return respuesta

def stark_marvel_app_3(lista):
    import os
    while True:
        imprimir_menu()
        opcion = stark_menu_principal()

        if opcion == '1':
            stark_imprimir_nombres_con_iniciales(lista)
        elif opcion == '2':
            stark_generar_codigos_heroes(lista)
        elif opcion == '3':
            stark_normalizar_datos(lista)
        elif opcion == '4':
            stark_imprimir_indice_nombre(lista)
        elif opcion == '5':
            stark_navegar_fichas(lista)
        elif opcion.lower() == 's':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
        os.system("pause")
        os.system("cls")

