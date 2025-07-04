# import pygame
# import copy

# pantalla = pygame.display.set_mode((500, 500))

# sonido_click = crear_sonido("Sonidos/Click.mp3", 1.0)
# sonido_fondo = crear_sonido("Sonidos/MiceOnVenus.mp3", 0.2)
# sonido_fondo.play(-1) 

# fondo_tierra = importar_imagen("Imagenes/fondo_tierra.jpg", (500, 500))
# fondo_madera = importar_imagen("Imagenes/madera_osc.png", (500, 500))
# fondo_piedra = importar_imagen("Imagenes/fondo_piedra.png", (500, 500))
# tablero_imagen = importar_imagen("Imagenes/tablero.png", (400, 120))

# rectangulo_c = pygame.image.load("Imagenes/rectan_mine_chico.png")
# rectangulo_l = pygame.image.load("Imagenes/rectan_mine_largo.png")

# fuente_grande = crear_font("Minecraft.ttf", 30)
# fuente_chica = crear_font("Minecraft.ttf", 15)

# rects_menu = {
#     "1": pygame.Rect(125, 150, 250, 50),
#     "2": pygame.Rect(125, 210, 250, 50),
#     "3": pygame.Rect(125, 270, 250, 50)
# }

# rects_juego = {
#     "a": pygame.Rect(15, 250, 100, 45),
#     "b": pygame.Rect(140, 250, 100, 45),
#     "c": pygame.Rect(265, 250, 100, 45),
#     "salir": pygame.Rect(390, 250, 100, 45)
# }

# rect_salida = pygame.Rect(400, 0, 100, 50)

# datos_individuales = {
#     "estado" : "Menu",
#     "usuario" : "",
#     "posicion" : 15,
#     "respuesta" : None,
#     "mensaje_error" : "",
#     "error_nombre" : "",
#     "copia_preguntas" : copy.deepcopy(preguntas),
#     "pregunta_actual" : None,
#     "seguir" : True
# }

# datos_base = copy.deepcopy(datos_individuales) 