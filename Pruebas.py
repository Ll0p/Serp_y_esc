import pygame
import Steve
import random
import copy
from CarpetaJuego.Datos import *
from CarpetaJuego.Funciones import *
from Preguntas import preguntas
from Colores import *

############################################

def importar_imagen(path: str, tamaño: tuple[int]):
    imagen = pygame.image.load(path)
    return pygame.transform.scale(imagen, tamaño)

def meter_fondo(pantalla, fondo) -> None:
    pantalla.blit(fondo, (0, 0))

def crear_font(fuente, tamaño):
    return pygame.font.Font(fuente, tamaño)

def dibujar_menu(pantalla, rect_largo, rect_chico, fuente) -> None:
    pantalla.blit(rect_largo, (50, 75))
    lista_y = [150, 210, 270]
    for y in lista_y:
        pantalla.blit(rect_chico, (125, y))
    
    textos = ["Serpientes y Escaleras", "Jugar", "Ver resultados", "Salir"]
    pos_x_txt = [80, 210, 145, 210]
    pos_y_txt = [87, 162, 222, 282]
    for i in range(len(textos)):
        pantalla.blit(fuente.render(textos[i], True, GRIS_MC), (pos_x_txt[i],pos_y_txt[i]))

def dibujar_juego(pantalla, rect_chico, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero, pregunta_actual):
    pantalla.blit(fondo_piedra, (0, 230))
    pantalla.blit(fondo_madera, (0, 310))
    pantalla.blit(tablero, (50, 65))

    # Líneas separadoras
    pygame.draw.line(pantalla, NEGRO, (0, 230), (500, 230), 10)
    pygame.draw.line(pantalla, NEGRO, (0, 310), (500, 310), 10)

    # Lineas dibujadas
    lista_x = [10, 135, 260, 385] 
    for x in lista_x:
        pygame.draw.rect(pantalla, NEGRO, (x, 245, 110, 55))

    # rects minecraft
    pos_rects = [15, 140, 265, 390]
    for x in pos_rects:
        pantalla.blit(rect_chico, (x,250))

    # Textos rects
    textos = ["A", "B", "C", "Salir"]
    pos_txt = [55, 180, 305, 410]
    for i in range(len(textos)):
        pantalla.blit(fuente_grande.render(textos[i], True, GRIS_MC), (pos_txt[i],260))

    if pregunta_actual != None:
        lista_y = [340,375,400,425]
        textos = [pregunta_actual["pregunta"], f"A: {pregunta_actual["respuesta_a"]}", f"B: {pregunta_actual["respuesta_b"]}", f"C: {pregunta_actual["respuesta_c"]}"]
        for i in range(len(lista_y)):
            pantalla.blit(fuente_chica.render(textos[i], True, GRIS_MC), (20, lista_y[i]))

def crear_sonido(path_sonido: str, volumen: float = 0.1) -> pygame.mixer.Sound:
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(path_sonido)
    sonido.set_volume(volumen)
    return sonido

def clickeo_en(rect: pygame.Rect, pos: tuple[int, int], sonido) -> bool:
    retorno = False
    if rect.collidepoint(pos):
        sonido.play()
        retorno = True
    return retorno

def mostrar_puntajes_pygame(pantalla, path, fuente):
    usuarios = parser_csv(path)
    usuarios_ordenados = ordenar_usuarios_descendente(usuarios)
    distancia = 20
    for i in range(len(usuarios_ordenados)):
        pantalla.blit(fuente.render(f"{i+1}° | Usuario: {usuarios_ordenados[i]["nombre"]} | Puntaje: {usuarios_ordenados[i]["puntaje"]}", True, GRIS_MC), (50,distancia))
        distancia += 20

############################################

pygame.init()
pantalla = pygame.display.set_mode((500, 500))

sonido_click = crear_sonido("Sonidos/Click.mp3", 1.0)
sonido_fondo = crear_sonido("Sonidos/MiceOnVenus.mp3", 0.2)
sonido_fondo.play(-1) 

fondo_tierra = importar_imagen("Imagenes/fondo_tierra.jpg", (500, 500))
fondo_madera = importar_imagen("Imagenes/madera_osc.png", (500, 500))
fondo_piedra = importar_imagen("Imagenes/fondo_piedra.png", (500, 500))
tablero_imagen = importar_imagen("Imagenes/tablero.png", (400, 120))

rectangulo_c = pygame.image.load("Imagenes/rectan_mine_chico.png")
rectangulo_l = pygame.image.load("Imagenes/rectan_mine_largo.png")

fuente_mc_grande = crear_font("Minecraft.ttf", 30)
fuente_mc_chico = crear_font("Minecraft.ttf", 15)

rects_menu = {
    "1": pygame.Rect(125, 150, 250, 50),
    "2": pygame.Rect(125, 210, 250, 50),
    "3": pygame.Rect(125, 270, 250, 50)
}

rects_juego = {
    "a": pygame.Rect(15, 250, 100, 45),
    "b": pygame.Rect(140, 250, 100, 45),
    "c": pygame.Rect(265, 250, 100, 45),
    "salir": pygame.Rect(390, 250, 100, 45)
}

rect_salida = pygame.Rect(400, 0, 100, 50)

dict_personaje = Steve.crear(50,65,40,40)

estado = "Menu"
usuario = ""
mensaje_error = ""
error_nombre = ""
posicion = 15
respuesta = None

copia_preguntas = copy.deepcopy(preguntas)
pregunta_actual = None

############################################

seguir = True
while seguir:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seguir = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Que evento.button == 1 significa que toqué click izquierdo
            if estado == "Menu":
                if clickeo_en(rects_menu["1"], evento.pos, sonido_click):
                    estado = "Ingreso"
                elif clickeo_en(rects_menu["2"], evento.pos, sonido_click):
                    estado = "Resultados"
                elif clickeo_en(rects_menu["3"], evento.pos, sonido_click):
                    seguir = False

            elif estado == "Ingreso" or estado == "Resultados":
                if clickeo_en(rect_salida, evento.pos, sonido_click):
                    estado = "Menu"

            elif estado == "Jugar":
                if clickeo_en(rects_juego["a"], evento.pos, sonido_click):
                    respuesta = "a"
                elif clickeo_en(rects_juego["b"], evento.pos, sonido_click):
                    respuesta = "b"
                elif clickeo_en(rects_juego["c"], evento.pos, sonido_click):
                    respuesta = "c"
                elif clickeo_en(rects_juego["salir"], evento.pos, sonido_click):
                    ingresar_datos_usuario(path, usuario, posicion)
                    usuario = "" # Podria resumirlo en una funcion como resetear_datos
                    posicion = 15
                    copia_preguntas = copy.deepcopy(preguntas)
                    pregunta_actual = None
                    estado = "Menu"
                    continue
                else:
                    respuesta = None # Porque sinó interpreta cualquier cosa

                if pregunta_actual != None and verificar_opcion(respuesta, ("a","b","c")):
                    posicion = modificar_posicion(tablero, posicion, verificar_respuesta(pregunta_actual, respuesta))
                    borde = verificar_ganador_perdedor_pygame(posicion, tablero)
                    if len(copia_preguntas) > 0 and not borde:
                        indice = random.randint(0, len(copia_preguntas) - 1)
                        pregunta_actual = retirar_pregunta(copia_preguntas, indice)
                    else:
                        ingresar_datos_usuario(path, usuario, posicion) 
                        usuario = "" # Podria resumirlo en una funcion como resetear_datos
                        posicion = 15
                        copia_preguntas = copy.deepcopy(preguntas)
                        pregunta_actual = None
                        estado = "Menu"

        elif evento.type == pygame.KEYDOWN and estado == "Ingreso":
            if evento.key == pygame.K_BACKSPACE:
                usuario = usuario[:-1] # Me devuelve el mismo texto menos el ultimo caracter
                mensaje_error = "" # Para que los errores no se vean en la pantalla, los reseteo
            elif evento.key == pygame.K_RETURN:
                if verificar_nombre(usuario): 
                    estado = "Jugar"
                    indice = random.randint(0, len(copia_preguntas) - 1)
                    pregunta_actual = retirar_pregunta(copia_preguntas, indice)
                else:
                    mensaje_error = "No puede usar este nombre"
            else:
                if evento.unicode.isalnum():
                    usuario += evento.unicode
                    mensaje_error = ""
                else:
                    mensaje_error = "Caracter no valido"

    meter_fondo(pantalla, fondo_tierra)

    if estado == "Menu":
        rect_chico = pygame.transform.scale(rectangulo_c, rects_menu["1"].size)
        rect_largo = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_menu(pantalla, rect_largo, rect_chico, fuente_mc_grande)

    elif estado == "Ingreso":
        rect_largo = pygame.transform.scale(rectangulo_l, (400, 50))
        rect_chico = pygame.transform.scale(rectangulo_c, rect_salida.size)
        pantalla.blit(rect_chico, (rect_salida.x, rect_salida.y))
        pantalla.blit(fuente_mc_grande.render("Salir",True,GRIS_MC), (420, 15))

        pantalla.blit(rect_largo, (40, 210))
        pantalla.blit(fuente_mc_grande.render(f"Nombre: {usuario}",True,GRIS_MC), (50, 220))
    
        if mensaje_error != "":
            pantalla.blit(fuente_mc_chico.render(mensaje_error, True, GRIS), (50, 270))

    elif estado == "Jugar":
        rect_chico = pygame.transform.scale(rectangulo_c, rects_juego["a"].size)
        dibujar_juego(pantalla, rect_chico, fuente_mc_grande, fuente_mc_chico, fondo_piedra, fondo_madera, tablero_imagen, pregunta_actual)
        # Steve.actualizar_pantalla(pantalla, dict_personaje)

    elif estado == "Resultados":
        rect_chico = pygame.transform.scale(rectangulo_c, rect_salida.size)
        pantalla.blit(rect_chico, (rect_salida.x, rect_salida.y))
        pantalla.blit(fuente_mc_grande.render("Salir",True,GRIS_MC), (420, 15))
        mostrar_puntajes_pygame(pantalla, "CarpetaJuego/Score.csv", fuente_mc_chico)

    pygame.display.flip()

sonido_fondo.stop()
pygame.quit()

### COSAS A TERMINAR ###

# AÑADIR PERSONAJE, SU INTERACCION CON EL TABLERO Y LAS TNT
# MODULARIZAR
# EVITAR LAS VARIABLES GLOBALES
# RESUMIR EN FUNCIONES
# OPTIMIZAR O SIMPLIFICAR LO QUE SE PUEDA