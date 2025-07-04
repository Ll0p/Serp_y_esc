from CarpetaJuego.Funciones import *
from CarpetaJuego.Datos import tablero, path
from Preguntas import preguntas

def juego(tablero: tuple[int], preguntas: list[dict[str, str]], path: str):
    seguir = True
    while seguir:
        mostrar_menu()
        opcion_menu = ingresar_respuesta_menu()

        if opcion_menu == "1":
            jugar_en_consola(tablero, preguntas, path)
        elif opcion_menu == "2":
            mostrar_puntajes(path)
        elif opcion_menu == "3":
            seguir = despedirse()
        elif opcion_menu == "4":
            jugar_pygame(preguntas, path, tablero)

jugar_pygame(preguntas, path, tablero)