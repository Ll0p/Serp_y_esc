import pygame
import random

################################## INTERACCIÓN_INGRESO ###################################

def interactuar_ingreso(evento, copia_preguntas: list[dict[str, str]], ):
    if evento.key == pygame.K_BACKSPACE:
        usuario = usuario[:-1] # Me devuelve el mismo texto menos el ultimo caracter
        mensaje_error = "" # Para que los errores no se vean en la pantalla, los reseteo
        error_nombre = ""
    elif evento.key == pygame.K_RETURN:
        if verificar_nombre(usuario): 
            estado = "Jugar"
            indice = random.randint(0, len(copia_preguntas) - 1)
            pregunta_actual = retirar_pregunta(copia_preguntas, indice)
        elif len(usuario) < 0:
            mensaje_error = "El nombre no puede estar vacío"
        else:
            error_nombre = "No puede usar este nombre"
    else:
        if evento.unicode.isalnum():
            usuario += evento.unicode
            mensaje_error = ""
        else:
            mensaje_error = "Caracter no válido"

##########################################################################################

####################################################################################################################################################################################

####################################### MENU_VISUAL ######################################

def meter_rectangulos_menu(pantalla, rectangulo_c, rectangulo_l) -> None:
    pantalla.blit(rectangulo_l, (50, 75))
    lista_pos_y = [150, 210, 270]
    for y in lista_pos_y:
        pantalla.blit(rectangulo_c, (125, y))

def mostrar_textos_menu(pantalla, fuente, color) -> None:
    textos = ["Serpientes y Escaleras", "Jugar", "Ver resultados", "Salir"]
    lista_pos_x = [80, 210, 145, 210]
    lista_pos_y = [87, 162, 222, 282]
    for i in range(len(textos)):
        pantalla.blit(fuente.render(textos[i], True, color), (lista_pos_x[i],lista_pos_y[i]))

def dibujar_menu(pantalla, rectangulo_c, rectangulo_l, fuente_grande) -> None:
    from Colores import GRIS_MC
    meter_rectangulos_menu(pantalla, rectangulo_c, rectangulo_l)
    mostrar_textos_menu(pantalla, fuente_grande, GRIS_MC)

##########################################################################################

###################################### JUEGO_VISUAL ######################################

def mostrar_fondos_juego(pantalla, fondo_piedra, fondo_madera, tablero_imagen) -> None:
    pantalla.blit(fondo_piedra, (0, 230))
    pantalla.blit(fondo_madera, (0, 310))
    pantalla.blit(tablero_imagen, (50, 65))

def dibujar_lineas_juego(pantalla, color: tuple) -> None:
    pygame.draw.line(pantalla, color, (0, 230), (500, 230), 10)
    pygame.draw.line(pantalla, color, (0, 310), (500, 310), 10)
    lista_x = [10, 135, 260, 385] 
    for x in lista_x:
        pygame.draw.rect(pantalla, color, (x, 245, 110, 55))

def meter_rectangulos_juego(pantalla, rectangulo_c) -> None:
    lista_pos_x = [15, 140, 265, 390]
    for x in lista_pos_x:
        pantalla.blit(rectangulo_c, (x,250))

def mostrar_textos_rects_juego(pantalla, fuente_grande, color: tuple) -> None:
    textos = ["A", "B", "C", "Salir"]
    lista_pos_x = [55, 180, 305, 410]
    for i in range(len(textos)):
        pantalla.blit(fuente_grande.render(textos[i], True, color), (lista_pos_x[i],260))

def mostrar_preguntas(pantalla, fuente_chica, color: tuple, pregunta_actual: dict[str, str]) -> None:
    lista_pos_y = [340, 375, 400, 425]
    textos = [pregunta_actual["pregunta"], f"A: {pregunta_actual["respuesta_a"]}", f"B: {pregunta_actual["respuesta_b"]}", f"C: {pregunta_actual["respuesta_c"]}"]
    for i in range(len(lista_pos_y)):
        pantalla.blit(fuente_chica.render(textos[i], True, color), (20, lista_pos_y[i]))

def dibujar_juego(pantalla, rectangulo_c, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero_imagen, pregunta_actual: dict[str, str]) -> None:
    from Colores import NEGRO, GRIS_MC
    mostrar_fondos_juego(pantalla, fondo_piedra, fondo_madera, tablero_imagen)
    dibujar_lineas_juego(pantalla, NEGRO)
    meter_rectangulos_juego(pantalla, rectangulo_c)
    mostrar_textos_rects_juego(pantalla, fuente_grande, GRIS_MC)
    if pregunta_actual != None:
        mostrar_preguntas(pantalla, fuente_chica, GRIS_MC, pregunta_actual)

##########################################################################################

##################################### INGRESO_VISUAL #####################################

def meter_rects_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida) -> None:
    pantalla.blit(rectangulo_c, (rect_salida.x, rect_salida.y))
    pantalla.blit(rectangulo_l, (40, 210))

def mostrar_textos_ingreso(pantalla, fuente, color: tuple, usuario: str) -> None:
    pantalla.blit(fuente.render("Salir",True,color), (420, 15))
    pantalla.blit(fuente.render(f"Nombre: {usuario}",True,color), (50, 220))

def mostrar_error_ingreso(pantalla, fuente, color: tuple, mensaje_error: str) -> None:
    pantalla.blit(fuente.render(mensaje_error, True, color), (50, 270))

def dibujar_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida, fuente_chica, fuente_grande, mensaje_error_vacio: str, mensaje_error_nombre: str, usuario: str) -> None:
    from Colores import GRIS, GRIS_MC
    meter_rects_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida)
    mostrar_textos_ingreso(pantalla, fuente_grande, GRIS_MC, usuario)
    if mensaje_error_vacio != "":
        mostrar_error_ingreso(pantalla, fuente_chica, GRIS, mensaje_error_vacio)
    elif mensaje_error_nombre != "":
        mostrar_error_ingreso(pantalla, fuente_chica, GRIS, mensaje_error_nombre)

##########################################################################################

#################################### RESULTADO_VISUAL ####################################

def mostrar_salida(pantalla, rectangulo_c, rect_salida, fuente_grande, color):
    pantalla.blit(rectangulo_c, (rect_salida.x, rect_salida.y))
    pantalla.blit(fuente_grande.render("Salir",True,color), (420, 15))

def mostrar_puntajes_pygame(pantalla, fuente, color, usuarios_ordenados: list[dict]) -> None:
    distancia = 20
    for i in range(len(usuarios_ordenados)):
        pantalla.blit(fuente.render(f"{i+1}° | Usuario: {usuarios_ordenados[i]["nombre"]} | Puntaje: {usuarios_ordenados[i]["puntaje"]}", True, color), (50,distancia))
        distancia += 20

def dibujar_resultados(pantalla, rectangulo_c, rect_salida, fuente_chica, fuente_grande, path) -> None:
    from Colores import GRIS_MC
    mostrar_salida(pantalla, rectangulo_c, rect_salida, fuente_grande, GRIS_MC)
    usuarios = parser_csv(path)
    usuarios_ordenados = ordenar_usuarios_descendente(usuarios)
    mostrar_puntajes_pygame(pantalla, fuente_chica, GRIS_MC, usuarios_ordenados)

######################################### VISUAL #########################################

def dibujar_visuales(pantalla, estado: str, rects_menu: dict, rects_juego: dict, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, mensaje_error: str, error_nombre: str, usuario: str, pregunta_actual:  dict[str, str], path: str) -> None:
    meter_fondo(pantalla, fondo_tierra)
    if estado == "Menu":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_menu["1"].size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_menu(pantalla, rectangulo_c, rectangulo_l, fuente_grande)

    elif estado == "Ingreso":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida, fuente_chica, fuente_grande, mensaje_error, error_nombre, usuario)

    elif estado == "Jugar":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_juego["a"].size)
        dibujar_juego(pantalla, rectangulo_c, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero_imagen, pregunta_actual)

    elif estado == "Resultados":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        dibujar_resultados(pantalla, rectangulo_c, rect_salida, fuente_chica, fuente_grande, path)

####################################################################################################################################################################################

def jugar_pygame():
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

    fuente_grande = crear_font("Minecraft.ttf", 30)
    fuente_chica = crear_font("Minecraft.ttf", 15)

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
    posicion = 15
    respuesta = None

    copia_preguntas = copy.deepcopy(preguntas)
    pregunta_actual = None

    ############################################

    seguir = True
    while seguir:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
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
                        continue # Para que no avance mas que hasta aca
                    else:
                        respuesta = None

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
                    elif len(usuario) < 0:
                        mensaje_error = "El nombre no puede estar vacío"
                    else:
                        error_nombre = "No puede usar este nombre"
                else:
                    if evento.unicode.isalnum():
                        usuario += evento.unicode
                        mensaje_error = ""
                    else:
                        mensaje_error = "Caracter no válido"

        meter_fondo(pantalla, fondo_tierra)

        dibujar_visuales(pantalla, estado, rects_menu, rects_juego, rect_salida, fuente_chica, fuente_grande, fondo_piedra, fondo_madera, tablero_imagen, mensaje_error, error_nombre, usuario, pregunta_actual, path)

        pygame.display.flip()

    sonido_fondo.stop()
    pygame.quit()