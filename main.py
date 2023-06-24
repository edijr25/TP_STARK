from funciones import *
from data_stark import lista_personajes
from stark_biblioteca01 import *
from stark_biblioteca03 import *
import os

while True:
    menu_principal = """
    -------- Menú ---------
    1. Obtener menú Stark 0 y 1
    2. Obtener menú Stark 02
    3. Obtener menú Stark 03
    4. Obtener menú Stark 04
    5. Salir
    """

    imprimir_dato(menu_principal)

    opción= (int(input("Ingrese una opción: ")))

    if opción == 1:
        menu(lista_personajes)

    elif opción == 2:
        menu2 = stark_menu_principal()
        stark_marvel_app (lista_personajes)
            
    elif opción == 3:
        stark_marvel_app_3 (lista_personajes)

    elif opción == 5:
        salida = input("Confirma salida (s/n):")
        if (salida == "s"):
            break 
    
    os.system("pause")
    os.system("cls")

