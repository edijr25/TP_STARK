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
    for heroe in lista:
        print(heroe['codigo_heroe'])



lista_personajes = [
    {
        "nombre": "Howard the Duck",
        "identidad": "Howard (Last name unrevealed)",
        "empresa": "Marvel Comics",
        "altura": "79.349999999999994",
        "peso": "18.449999999999999",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Yellow",
        "fuerza": "2",
        "inteligencia": ""
    },
    {
        "nombre": "Spider-Man",
        "identidad": "Peter Benjamin Parker",
        "empresa": "Marvel Comics",
        "altura": "178",
        "peso": "76",
        "genero": "M",
        "color_ojos": "Hazel",
        "color_pelo": "Brown",
        "fuerza": "3",
        "inteligencia": "4"
    },
    {
        "nombre": "Captain Marvel",
        "identidad": "Carol Danvers",
        "empresa": "Marvel Comics",
        "altura": "180",
        "peso": "74",
        "genero": "F",
        "color_ojos": "Blue",
        "color_pelo": "Blonde",
        "fuerza": "5",
        "inteligencia": "3"
    }
]

stark_generar_codigos_heroes(lista_personajes)
##for heroe in lista_personajes:
    ##print (heroe)
