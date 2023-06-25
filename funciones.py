from data_stark import lista_personajes
from stark_biblioteca01 import *

def menu (lista):
    import os
    while True:
        print("-----Menu de opciones------")
        print("1.- Imprimir lista con datos")
        print("2.- Imprimir nombre de cada superheroe")
        print("3.- Imprimir nombre y altura de cada heroe")
        print("4.- Heroe mas alto")
        print("5.- Heroe mas bajo")
        print("6.- Altura promedio de los superheroes")
        print("7.- Heroe mas pesado")
        print("8.- Heroe menos pesado")
        print("9.- Nombre de heroes Masculinos")
        print("10.- Nombre de heroes Femeninos")
        print("11.- Heroe mas bajo genero M")
        print("12.- Heroe mas bajo genero F")
        print("13.- Heroe mas alto genero M")
        print("14.- Heroe mas alto genero F")
        print("15.- Promedio de la altura de heroes masculinos")
        print("16.- Promedio de la altura de heroes femeninos")
        print("17.- Informar nombres de la opción 11-12-13-14")
        print("18.- Informar cantidad de superheroes segun su color de ojos")
        print("19.- Informar cantidad de superheroes segun su color de pelo")
        print("20.- Informar cantidad de superheroes segun su inteligencia")
        print("21.- Nombres segun su color de ojos")
        print("22.- Nombres segun su color de pelo")
        print("23.- Nombres segun su inteligencia")
        print("24.- Salir")
        
        opción= (int(input("Ingrese una opción: ")))

        if opción == 1:
            mostrar_lista (lista, "Lista de superHeroes")
            stark_normalizar_datos (lista)

        elif opción == 2:
            stark_imprimir_nombres_heroes(lista)
            
        elif opción == 3:
            stark_imprimir_nombres_alturas (lista)

        elif opción == 4:
            stark_calcular_imprimir_heroe(lista,"maximo","altura")
            ##alturaMaxima= proyectar_heroe (lista, "altura")
            #max = alturaMax (alturaMaxima)
            #print ("La altura maxima es ", max)

        elif opción == 5:
            stark_calcular_imprimir_heroe(lista, "minimo", "altura")
            ##alturaMinima = proyectar_heroe (lista, "altura")
            ##min = alturaMin (alturaMinima)
            ##print ("La altura minima es {}".format(min))


        elif opción == 6:
            stark_calcular_imprimir_promedio_altura (lista)
            ##promedio = proyectar_heroe (lista, "altura")
            ##promedio = promedioAltura (promedio)
            ##print ("La altura promedio es {:.3f}".format(promedio))    

        elif opción == 7:
            stark_calcular_imprimir_heroe(lista,"maximo","peso")
            ##masPesado = proyectar_heroe (lista, "peso")  
            ##masPesado = heroeMasPesado (masPesado)
            ##print("El heroe mas pesado pesa {:.3f}".format (masPesado))

        elif opción == 8:
            stark_calcular_imprimir_heroe(lista,"minimo","peso")
            ##menosPesado = proyectar_heroe (lista, "peso")  
            ##menosPesado = heroeMasPesado (menosPesado)
            ##print("El heroe menos pesado pesa {:.3f}".format (menosPesado))

        elif opción == 10:
            femeninos = filtrar_heroes(lista, "genero", "F")
            femeninos = proyectar_heroe(femeninos, "nombre")
            mostrar_lista(femeninos, "Heroes Femeninas")

        elif opción == 9:
            masculinos = filtrar_heroes(lista, "genero", "M")
            masculinos = proyectar_heroe(masculinos, "nombre")
            mostrar_lista(masculinos, "Heroes Masculinos")    
        
        elif opción == 11:
            altura_baja_m = filtrar_heroes(lista, "genero", "M")
            masculino = proyectar_heroe (altura_baja_m, "altura")
            masculino = alturaMin (masculino)
            print ("La altura mas baja de los heroes masculinos es {:.3f}" .format (masculino))

        elif opción == 12:
            altura_baja_f = filtrar_heroes(lista, "genero", "F")
            femenino = proyectar_heroe (altura_baja_f, "altura")
            femenino = alturaMin (femenino)
            print ("La altura mas baja de los heroes femeninos es {:.3f}" .format (femenino))
    
        elif opción == 13:
            altura_alta_m = filtrar_heroes(lista, "genero", "M")
            masculino = proyectar_heroe (altura_alta_m, "altura")
            masculino = alturaMax (masculino)
            print ("La altura mas alta de los heroes masculinos es {:.3f}" .format (masculino))        
        
        elif opción == 14:
            altura_alta_f = filtrar_heroes(lista, "genero", "F")
            femenino = proyectar_heroe (altura_alta_f, "altura")
            femenino = alturaMax (femenino)
            print ("La altura mas alta de los heroes femeninos es {:.3f}" .format (femenino))
        
        elif opción == 15:
            promedio_m = filtrar_heroes(lista, "genero", "M")
            masculino = proyectar_heroe (promedio_m, "altura")
            masculino = promedioAltura(masculino)
            print ("El promedio de los heroes masculino es {:.3f}" .format (masculino))
        
        elif opción == 16:
            promedio_f = filtrar_heroes(lista, "genero", "F")
            femenino = proyectar_heroe (promedio_f, "altura")
            femenino = promedioAltura(femenino)
            print ("El promedio de los heroes femeninos es {:.3f}" .format (femenino))
        
        elif opción == 17:
            fem_min = filtrar_heroes (lista, "genero", "F")
            stark_calcular_imprimir_heroe(fem_min,"minimo","altura")
            fem_max = filtrar_heroes (lista, "genero", "F")
            stark_calcular_imprimir_heroe(fem_max,"maximo","altura")
            men_min = filtrar_heroes(lista, "genero", "M")
            stark_calcular_imprimir_heroe(men_min,"minimo","altura")
            men_max = filtrar_heroes (lista, "genero", "M")
            stark_calcular_imprimir_heroe(men_max,"maximo","altura")
            
        elif opción == 18:
            color_ojos =proyectar_heroe(lista, "color_ojos")
            contar_colores(color_ojos,"Colores de ojos")    
            
        elif opción == 19:
            color_pelo = proyectar_heroe(lista, "color_pelo")
            contar_colores(color_pelo, "Colores Pelos")    

        elif opción == 20:
            inteligencia = proyectar_heroe(lista, "inteligencia")
            contar_colores(inteligencia, "Inteligencia") 
        
        elif opción == 21:
            agrupar_por_tipo (lista, "color_ojos", "Color de ojos")   
    
        elif opción == 22:
            agrupar_por_tipo (lista, "color_pelo", "Color de pelo")   

        elif opción == 23:
            agrupar_por_tipo (lista, "inteligencia", "Tipo de Inteligencia")   


        elif opción == 24:
            salida = input("Confirma salida (s/n):")
            if (salida == "s"):
                break 
        os.system("pause")
        os.system("cls")


## Funcion proyectar_heroe (lista : list, key: str) -> list:
##Se encarga de mostrar una lista filtrada
##Recibe parametros list, str e imprime una list
def proyectar_heroe (lista : list, key: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe [key])
    return lista_filtrada


def mostrar_lista (lista: list, title: str )-> None:
    print(f"      ***   {title}   ***")
    for item in lista:
        print (item)

##Funcion alturaMax (lista) --> String,float
##Se encarga de mostrar el nombre y altura del heroe mas alto
##Recibe un parametro tipo lista e imprime un string y un float
def alturaMax (lista):
    altura_maxima = 0

    for superheroe in lista:
        altura = float(superheroe)
        if altura > altura_maxima:
            altura_maxima = altura
            
    return altura_maxima

##Funcion alturaMin (lista) --> String,float
##Se encarga de mostrar el nombre y altura del heroe mas bajo
##Recibe un parametro tipo lista e imprime un string y un float
def alturaMin (lista):
    altura_min = float(lista[0]) 

    for superheroe in lista:
        altura = float (superheroe)
   
        if altura < altura_min:
            altura_min = altura
            
    return altura_min

##Funcion mostrar_nombreAltura_heroes (lista) -->String,float
##Se encarga de mostrar el nombre y altura de los heroes
##Recibe un parametro tipo lista e imprime un string y un float
def mostrar_nombreAltura_heroes(lista):
    for superHeroe in lista:
        altura_float = float(superHeroe["altura"])
        print("Nombre del superhéroe es {}, la altura es {:.3f} cm".format(superHeroe["nombre"], altura_float))

#Funcion promedioAltura (lista) --> float
##Se encarga de mostrar la altura promedio de los superheroes
##Recibe un parametro tipo lista e imprime un float
def promedioAltura(lista):
    contadorAltura = 0
    for superheroe in lista:
       altura = float (superheroe)
       contadorAltura = contadorAltura + altura

    promedioAlturaHeroes = contadorAltura / len(lista)
    
    return promedioAlturaHeroes

##Funcion heroeMasPesado (lista) --> String,float
##Se encarga de mostrar el nombre y peso del heroe mas pesado
##Recibe un parametro tipo lista e imprime un float
def heroeMasPesado (lista):
    pesoMax = float (lista[0])

    for superheroe in lista:
        peso = float(superheroe)
    
        if peso > pesoMax:
            pesoMax = peso
            
    return pesoMax

##Funcion heroeMenosPesado (lista) --> String,float
##Se encarga de mostrar el nombre y peso del heroe menos pesado
##Recibe un parametro tipo lista e imprime un string y un float
def heroeMenosPesado (lista):

    pesoMin = float(lista[0]) 
    
    for superheroe in lista:
        peso = float (superheroe)
        
        if peso < pesoMin:
            pesoMin = peso
            
    return pesoMin


##Función filtrar_heroes (lista: list, key: str, color: str) -> list:
##Se encarga de filtrar y crear una lista con los valores que se le asignan
##Recibe parametros tipo list, str, str e imprime una list
def filtrar_heroes (lista: list, key: str, color: str) -> list:
    lista_filtrada = []
    for heroe in lista:
        if (heroe[key] == color):
            lista_filtrada.append (heroe)
    return lista_filtrada

## Funcion contar_colores(lista: str, title: str) ->None:
## se encargar de contar los colores e imprimirlos en forma de tabla
##Recibe como parametros una list, str
def contar_colores(lista: list, title: str) ->None:
    contador_colores = {}
    for color_ojos in lista:
        if color_ojos in contador_colores:
            contador_colores[color_ojos] += 1
        else:
            contador_colores[color_ojos] = 1
    if '' in contador_colores:
        contador_colores['No tiene'] = contador_colores.pop('')
    else:
        contador_colores['No tiene'] = 0
    
    # Imprimir los resultados en columnas
    print(f" {title}   |   Cantidad")
    print("----------------|----------")
    for color, cantidad in contador_colores.items():
        print(f"{color:<15} |   {cantidad}")

##Funcion agrupar_por_tipo (lista: str, key: str, title:str)->:
## se encarga de agrupar los superHeroes segun el parametro que le pasen
##ya sea color de pelo, color de ojos, tipo de inteligencia e imprime el mismo segun el grupo y su nombre
def agrupar_por_tipo (lista, key, title):
    grupos = {}
    for heroe in lista:
        color_pelo = heroe[f"{key}"]
        if color_pelo in grupos:
            grupos[color_pelo].append(heroe)
        else:
            grupos[color_pelo] = [heroe]
    for color, grupo in grupos.items():
        print(f"{title}: {color}")
        for heroe in grupo:
            print(f"- {heroe['nombre']}")
        print("--------")


def mostrar_lista (lista: list, title: str )-> None:
    print(f"      ***   {title}   ***")
    for item in lista:
        print (item)
        print ("")
