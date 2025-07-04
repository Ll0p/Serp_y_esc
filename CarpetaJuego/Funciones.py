def consultar_nombre() -> str:
    """ Consulta al usuario su nombre y lo retorna

    Retorna:
        str: El nombre ingresado con capitalize
    """
    usuario = input("\nIngrese su nombre: ").capitalize()
    return usuario

def preguntar_seguir() -> str:
    """ Pregunta al usuario si desea continuar y devuelve la respuesta

    Retorna:
        str: La respuesta ingresada en minusculas
    """
    seguir = input("\n¿ Desea seguir intentando [si/no]? : ").lower()
    return seguir

def consultar_opcion() -> str:
    """ Consulta al usuario para que elija una opcion y la retorna

    Retorna:
        str: La opción ingresada en minusculas
    """
    opcion = input("\nElija una opción: ").lower()
    return opcion 

###################################################################

def verificar_longitud_nombre(cadena: str) -> bool:
    """ Verifica que la longitud de la cadena sea existente

    Argumento:
        cadena (str): Cadena de texto a verificar

    Retorna:
        bool: True en caso de existir una longitud y viceversa
    """
    return len(cadena.strip()) > 0

def verificar_existencia_score(path_csv, nombre: str) -> bool:
    """ Verifica si el usuario existe en el archivo y retorna un booleano

    Argumentos:
        path (_type_): Path del archivo.csv
        nombre (str): Nombre a verificar

    Retorna:
        bool: True en caso de que el nombre exista en el archivo y viceversa
    """
    encontrado = False
    try:
        with open(path_csv, "r", encoding = "UTF-8") as archivo:
            for linea in archivo:
                if linea.split(",")[0] == nombre:
                    encontrado = True
                    break
    except FileNotFoundError:
        print("El archivo no existe")
        encontrado = False
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")
    return encontrado

def verificar_nombre(nombre: str) -> bool:
    """ Verifica que el nombre sea válido y no esté repetido.

    Argumentos:
        nombre (str): Nombre a verificar

    Retorna:
        bool: True en caso de que se cumplan ambas condiciones y viceversa
    """
    from CarpetaJuego.Datos import path
    return verificar_longitud_nombre(nombre) and not verificar_existencia_score(path, nombre)

def verificar_seguir(decision: str) -> bool:
    """ Verifica que la decisión es igual a "si" o "no" y retorna un booleano en base a eso

    Argumentos:
        decision (str): Una cadena a analizar

    Retorna:
        bool: True en caso de ser una de las opciones y viceversa
    """
    verificado = True
    if decision.strip() != "si" and decision.strip() != "no":
        verificado = False
    return verificado

def verificar_opcion(opcion_elegida: str, opciones: tuple[str]) -> bool:
    """ Verifica si la opción elegida se encuentra en una lista de opciones

    Argumentos:
        opcion_elegida (str): La opción que se quiere verificar
        opciones (tuple[str]): La lista de opciones posibles/existentes

    Retorna:
        bool: True en caso de que la opcion exista en la lista pasada y viceversa
    """
    encontrado = False
    for opcion in opciones:
        if opcion == opcion_elegida:
            encontrado = True
            break
    return encontrado

def verificar_opcion_menu(opcion: str) -> bool:
    from CarpetaJuego.Datos import opciones_menu
    return verificar_opcion(opcion, opciones_menu)

def verificar_opcion_respuestas(opcion: str) -> bool:
    from CarpetaJuego.Datos import opciones_respuesta
    return verificar_opcion(opcion, opciones_respuesta)

def verificar_respuesta(pregunta: dict[str,str], respuesta: str) -> bool:
    """ Verifica si la respuesta es correcta

    Argumentos:
        pregunta (dict[str,str]): La pregunta 
        respuesta (str): La respuesta

    Retorna:
        bool: True si es correcta y viceversa
    """
    return respuesta == pregunta["respuesta_correcta"]

def verificar_ganador_perdedor(posicion: int, tablero: tuple[int]) -> bool:
    """ Verifica si ganaste o perdiste

    Argumentos:
        posicion (int): La posicion del jugador
        tablero (tuple[int]): El tablero del juego

    Retorna:
        bool: False si ganaste o perdiste
    """
    retorno = True
    if posicion <= 0:
        print("\nPerdiste... caíste en la casilla 0. :/")
        retorno = False
    elif posicion >= (len(tablero) - 1):
        print("\nFelicidades, ¡Ganaste! <3")
        retorno = False
    return retorno 

def verificar_ganador_perdedor_pygame(posicion: int, tablero: tuple[int]) -> bool:
    """ Verifica si ganaste o perdiste

    Argumentos:
        posicion (int): La posicion del jugador
        tablero (tuple[int]): El tablero del juego

    Retorna:
        bool: True si ganaste o perdiste
    """
    retorno = False
    if posicion <= 0 or posicion >= (len(tablero) - 1):
        retorno = True
    return retorno 

###################################################################

def ingresar_respuesta(input: callable, verificador: callable) -> str: # No se si puedo importar "Callable", para especificar que tipo de funcion llamar.
    """ Solicita al usuario un input y la valida con una función.

    Argumentos:
        input (callable): Una función que le solicita al usuario
        verificador (callable): Una función que verifica el input

    Retorna:
        str: La respuesta ingresada por el usuario
    """
    respuesta = input()
    while not verificador(respuesta):
        print("Respuesta no valida, vuelva a intentar...")
        respuesta = input()
    return respuesta

def preguntar_salir() -> bool:
    """ Pregunta si queres seguir jugando

    Retorna:
        bool: True si queres seguir y viceversa
    """
    respuesta = ingresar_respuesta(preguntar_seguir, verificar_seguir)
    return respuesta == "si"

def ingresar_respuesta_menu() -> str:
    return ingresar_respuesta(consultar_opcion, verificar_opcion_menu)

###################################################################

def mostrar_pregunta(pregunta: dict[str, str]) -> None:
    """ Muestra la pregunta y sus opciones

    Argumentos:
        pregunta (dict[str, str]): Pregunta a mostrar
    """
    print(f"\n{pregunta['pregunta']}")
    print(f"Opcion a: {pregunta['respuesta_a']}")
    print(f"Opcion b: {pregunta['respuesta_b']}")
    print(f"Opcion c: {pregunta['respuesta_c']}")

def retirar_pregunta(preguntas: list[dict[str, str]], indice_pregunta: int) -> dict[str, str]:
    """ Retira una pregunta

    Argumentos:
        preguntas (list[dict[str, str]]): La lista de preguntas
        indice_pregunta (int): El indice de la pregunta

    Retorna:
        dict[str, str]: La pregunta eliminada (por si las dudas)
    """
    return preguntas.pop(indice_pregunta)

###################################################################

def mostrar_menu() -> None:
    """ Muestra el menú """
    print("\n----- Bienvenido a Serpientes y escaleras -----")
    print("1. Jugar")
    print("2. Ver puntajes")
    print("3. Salir")
    print("4. Jugar versión Pygame")

def imprimir_lineas() -> None:
    """ Imprime una linea """
    print(f"\n{"-" * 50}")

###################################################################

def limitar_posicion(posicion: int, tablero: tuple[int]) -> int:
    """Asegura que la posición se mantenga dentro del rango del tablero."""
    if posicion < 0:
        posicion = 0
    elif posicion >= len(tablero):
        posicion = len(tablero) - 1
    return posicion

def mover_por_respuesta(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Avanza o retrocede en base a la respuesta

    Argumentos:
        posicion (int): Posición actual del jugador.
        respuesta_verificada (bool): True si respondió bien y viceversa
        largo_tablero (int): Longitud total del tablero.

    Retorna:
        int: Nueva posición
    """
    if respuesta_verificada:
        posicion += 1
    else:
        posicion -= 1
    return limitar_posicion(posicion, tablero)

def aplicar_efecto_casilla(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Aplica escalera o serpiente (solo si es necesario).

    Argumentos:
        tablero (tuple[int]): EL tablero con efectos.
        posicion (int): Posición actual del jugador.
        respuesta_verificada (bool): True si respondió bien y viceversa

    Retorna:
        int: Nueva posición con efecto (si es necesario)
    """
    casilla = tablero[posicion]

    if casilla != 0:
        if respuesta_verificada:
            posicion += casilla
        else:
            posicion -= casilla
    return limitar_posicion(posicion, tablero)

def modificar_posicion(tablero: tuple[int], posicion: int, respuesta_verificada: bool) -> int:
    """ Modifica la posición y si hay, el efecto de la casilla

    Argumentos:
        tablero (tuple[int]): El tablero del juego
        posicion (int): Posición actual del usuario
        respuesta_verificada (bool): True en caso de responder bien y viceversa

    Retorna:
        int: La posición modificada
    """
    posicion = mover_por_respuesta(tablero, posicion, respuesta_verificada)
    posicion = aplicar_efecto_casilla(tablero, posicion, respuesta_verificada)
    return posicion

def mostrar_tablero(tablero: tuple[int], posicion: int) -> None:
    """ Muestra el tablero 

    Argumentos:
        tablero (tuple[int]): El tablero a mostrar
        posicion (int): La posición actual del jugador
    """
    print("\n----- TABLERO -----\n")
    for i in range(len(tablero)):
        casillero = ""
        if i == posicion:
            casillero += "[X]"  
        elif tablero[i] != 0:
            casillero += f"[{tablero[i]}]"
        else:
            casillero += "[ ]"

        print(f"{i} : {casillero}", end="  ")
        if (i + 1) % 5 == 0: # Para que se vea como un cuadrado en pantalla
            print(end = "\n")
    print(end = "\n") # Ya sé que sería lo mismo que no poner nada

###################################################################

def ingresar_datos_usuario(path, nombre: str, puntaje: int) -> None:
    """ Ingresa los datos del usuario al archivo

    Argumentos:
        path (_type_): Path del archivo
        nombre (str): Nombre del usuario
        puntaje (int): Puntaje del usuario
    """
    try:
        with open(path, "a", encoding = "UTF-8") as archivo:
            archivo.write(f"{nombre},{puntaje}\n")
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")

def parser_csv(path) -> list[dict]:
    """ Guarda los datos del archivo en un diccionario

    Argumentos:
        path (_type_): Ruta del archivo csv

    Retorna:
        list: Lista con diccionarios de nombre y puntajes de los jugadores
    """
    lista = []
    try:
        with open(path, "r", encoding = "UTF-8") as archivo:
            for linea in archivo:
                persona = {}
                lectura = linea.split(",")
                persona['nombre'] = lectura[0]
                persona['puntaje'] = int(lectura[1])
                lista.append(persona)
    except FileNotFoundError:
        print("No hay puntajes guardados")
    except Exception as excepcion:
        print(f"Algo salió mal: {excepcion}")

    return lista

def ordenar_usuarios_descendente(lista_csv: list[dict], criterio: str = 'puntaje'):
    """ Ordena la lista de jugadores de mayor a menor por criterio

    Argumentos:
        lista_csv (list[dict]): Lista de jugadores

    Retorna:
        list[dict]: Copia de la lista pero ordenada.
    """
    import copy
    csv_copia = copy.deepcopy(lista_csv)
    for i in range(len(csv_copia) - 1):
        for j in range(i + 1, len(csv_copia)):
            if csv_copia[i][criterio] < csv_copia[j][criterio]:
                aux = csv_copia[i]
                csv_copia[i] = csv_copia[j]
                csv_copia[j] = aux
    return csv_copia

def mostrar_usuarios_ordenados(usuarios_ordenados: list[dict]) -> None:
    """ Muesra los usuarios ordenados

    Argumentos:
        usuarios_ordenados (list[dict]): Lista ordenada de usuarios
    """
    if len(usuarios_ordenados) > 0:
        print("\n----- JUGADORES ORDENADOS -----")
        for i in range(len(usuarios_ordenados)):
            print(f"{i+1}° | Usuario: {usuarios_ordenados[i]['nombre']} | Puntaje: {usuarios_ordenados[i]['puntaje']}")
    else:
        print("\n----- No hay jugadores -----")

def mostrar_puntajes(path) -> None:
    """ Muestra los puntajes ordenados y decorado

    Argumentos:
        path (_type_): Path del archivo
    """
    usuarios = parser_csv(path)
    usuarios_ordenados = ordenar_usuarios_descendente(usuarios)
    imprimir_lineas()
    mostrar_usuarios_ordenados(usuarios_ordenados)
    imprimir_lineas()

###################################################################

def mostrar_game_over():
    """ Muestra game over al usuario en caso de que haya agotado las preguntas"""
    print("\n¡Te quedaste sin preguntas!")
    print("----- GAME OVER -----")

def jugar_en_consola(tablero: tuple[int], preguntas: list[dict[str, str]], path: str) -> None:
    """ Ejecuta el juego

    Argumentos:
        tablero (tuple[int]): El tablero del juego
        preguntas (list[dict[str, str]]): Lista de preguntas
    """
    import random
    import copy
    posicion = 15 # O len(tablero) // 2
    copia_preguntas = copy.deepcopy(preguntas)

    nombre = ingresar_respuesta(consultar_nombre, verificar_nombre)

    seguir = True
    while seguir and len(copia_preguntas) > 0:
        indice = random.randint(0, len(copia_preguntas) - 1) # Me va a generar un numero random entre 0-len(preguntas) (menos 1 porque es una lista)
        pregunta = retirar_pregunta(copia_preguntas, indice)

        mostrar_tablero(tablero, posicion)
        mostrar_pregunta(pregunta)
        respuesta = ingresar_respuesta(consultar_opcion, verificar_opcion_respuestas)
        posicion = modificar_posicion(tablero, posicion, verificar_respuesta(pregunta, respuesta))

        seguir = verificar_ganador_perdedor(posicion, tablero)
        if seguir and len(copia_preguntas) > 0:  
            seguir = preguntar_salir()

    if len(copia_preguntas) == 0:
        mostrar_game_over()

    ingresar_datos_usuario(path, nombre, posicion)

###################################################################

def despedirse() -> bool:
    """ Se despide del usuario

    Retorna:
        bool: False
    """
    print("\n¡ Nos vemos !")
    return False

import pygame

def clickeo_en(rect: pygame.Rect, pos: tuple[int, int], sonido) -> bool:
    retorno = False
    if rect.collidepoint(pos):
        sonido.play()
        retorno = True
    return retorno

def importar_imagen(path: str, tamaño: tuple[int]):
    imagen = pygame.image.load(path)
    return pygame.transform.scale(imagen, tamaño)

def meter_fondo(pantalla, fondo) -> None:
    pantalla.blit(fondo, (0, 0))

def crear_font(fuente, tamaño):
    return pygame.font.Font(fuente, tamaño)

def crear_sonido(path_sonido: str, volumen: float = 0.1) -> pygame.mixer.Sound:
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(path_sonido)
    sonido.set_volume(volumen)
    return sonido

################################### INTERACCIÓN_MOUSE ####################################

def resetear_datos(datos_indiv: dict, datos_base: dict) -> None:
    import copy
    for clave in datos_indiv:
        datos_indiv[clave] = copy.deepcopy(datos_base[clave])

def interaccion_mouse(evento, rects_menu: dict, rects_juego: dict, rect_salida, sonido_click, tablero: tuple[int], path: str, datos_indiv: dict, datos_base: dict) -> None:
    import random
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Que evento.button == 1 significa que toqué click izquierdo
        if datos_indiv["estado"] == "Menu":
            if clickeo_en(rects_menu["1"], evento.pos, sonido_click):
                datos_indiv["estado"] = "Ingreso"
            elif clickeo_en(rects_menu["2"], evento.pos, sonido_click):
                datos_indiv["estado"] = "Resultados"
            elif clickeo_en(rects_menu["3"], evento.pos, sonido_click):
                datos_indiv["seguir"] = False

        elif datos_indiv["estado"] == "Ingreso" or datos_indiv["estado"] == "Resultados":
            if clickeo_en(rect_salida, evento.pos, sonido_click):
                datos_indiv["estado"] = "Menu"

        elif datos_indiv["estado"] == "Jugar":
            datos_indiv["respuesta"] = datos_base["respuesta"]
            if clickeo_en(rects_juego["a"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "a"
            elif clickeo_en(rects_juego["b"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "b"
            elif clickeo_en(rects_juego["c"], evento.pos, sonido_click):
                datos_indiv["respuesta"] = "c"
            elif clickeo_en(rects_juego["salir"], evento.pos, sonido_click):
                ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"])
                resetear_datos(datos_indiv, datos_base)
                return None

            if datos_indiv["pregunta_actual"] != None and verificar_opcion(datos_indiv["respuesta"], ("a","b","c")):
                datos_indiv["posicion"] = modificar_posicion(tablero, datos_indiv["posicion"], verificar_respuesta(datos_indiv["pregunta_actual"], datos_indiv["respuesta"]))
                borde = verificar_ganador_perdedor_pygame(datos_indiv["posicion"], tablero)
                if len(datos_indiv["copia_preguntas"]) > 0 and not borde:
                    indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
                    datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)
                else:
                    ingresar_datos_usuario(path, datos_indiv["usuario"], datos_indiv["posicion"]) 
                    resetear_datos(datos_indiv, datos_base)


####################################################################################################################################################################################

############################## INTERACCIÓN_INGRESO_TECLADO ###############################

def borrar_letra(usuario: str) -> str:
    return usuario[:-1]

def verificar_alnum(caracter: str) -> bool:
    return caracter.isalnum()

def mensaje_caracter(caracter: str) -> str:
    mensaje = ""
    if not verificar_alnum(caracter):
        mensaje = "Caracter no valido"
    return mensaje

def interactuar_ingreso_teclado(evento, datos_indiv: dict) -> None:
    import random
    if evento.type == pygame.KEYDOWN and datos_indiv["estado"] == "Ingreso":
        if evento.key == pygame.K_BACKSPACE:
            datos_indiv["usuario"] = borrar_letra(datos_indiv["usuario"])
            datos_indiv["mensaje_error"] = ""
        elif evento.key == pygame.K_RETURN:
            if verificar_nombre(datos_indiv["usuario"]):
                datos_indiv["estado"] = "Jugar"
                indice = random.randint(0, len(datos_indiv["copia_preguntas"]) - 1)
                datos_indiv["pregunta_actual"] = retirar_pregunta(datos_indiv["copia_preguntas"], indice)
                datos_indiv["mensaje_error"] = ""
            else:
                datos_indiv["mensaje_error"] = "No puede usar este nombre"
        else:
            datos_indiv["mensaje_error"] = mensaje_caracter(evento.unicode)
            if datos_indiv["mensaje_error"] == "":
                datos_indiv["usuario"] += evento.unicode

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

def dibujar_visuales(pantalla, rectangulo_c, rectangulo_l, rects_menu: dict, rects_juego: dict, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, path: str, datos_indiv: dict) -> None:
    meter_fondo(pantalla, fondo_tierra)
    if datos_indiv["estado"] == "Menu":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_menu["1"].size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_menu(pantalla, rectangulo_c, rectangulo_l, fuente_grande)

    elif datos_indiv["estado"] == "Ingreso":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        rectangulo_l = pygame.transform.scale(rectangulo_l, (400, 50))
        dibujar_ingreso(pantalla, rectangulo_c, rectangulo_l, rect_salida, fuente_chica, fuente_grande, datos_indiv["mensaje_error"], datos_indiv["error_nombre"], datos_indiv["usuario"])

    elif datos_indiv["estado"] == "Jugar":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rects_juego["a"].size)
        dibujar_juego(pantalla, rectangulo_c, fuente_grande, fuente_chica, fondo_piedra, fondo_madera, tablero_imagen, datos_indiv["pregunta_actual"])

    elif datos_indiv["estado"] == "Resultados":
        rectangulo_c = pygame.transform.scale(rectangulo_c, rect_salida.size)
        dibujar_resultados(pantalla, rectangulo_c, rect_salida, fuente_chica, fuente_grande, path)

####################################################################################################################################################################################

def jugar_pygame(preguntas, path, tablero) -> None:
    import copy
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

    datos_individuales = {
        "estado" : "Menu",
        "usuario" : "",
        "posicion" : 15,
        "respuesta" : None,
        "mensaje_error" : "",
        "error_nombre" : "",
        "copia_preguntas" : copy.deepcopy(preguntas),
        "pregunta_actual" : None,
        "seguir" : True
    }

    datos_base = copy.deepcopy(datos_individuales) 

    while datos_individuales["seguir"]:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                datos_individuales["seguir"] = False
            interaccion_mouse(evento, rects_menu, rects_juego, rect_salida, sonido_click, tablero, path, datos_individuales, datos_base)
            interactuar_ingreso_teclado(evento, datos_individuales)

        dibujar_visuales(pantalla, rectangulo_c, rectangulo_l, rects_menu, rects_juego, rect_salida, fuente_chica, fuente_grande, fondo_tierra, fondo_piedra, fondo_madera, tablero_imagen, path, datos_individuales)

        pygame.display.flip()

    sonido_fondo.stop()
    pygame.quit()