import pygame 

def crear(x,y,ancho,alto):
    dict_personaje = {}
    dict_personaje["imagen"] = pygame.image.load("Imagenes/steve.png")
    dict_personaje["imagen"] = pygame.transform.scale(dict_personaje["imagen"], (ancho, alto))
    dict_personaje["rect_pos"] = pygame.Rect(x, y, ancho, alto)
    dict_personaje["score"] = 0
    return dict_personaje

def actualizar_pantalla(pantalla, dict_personaje):
    pantalla.blit(dict_personaje["imagen"], dict_personaje["rect_pos"])

def update_x(personaje, incremento_x):
    pared = True
    nueva_x = personaje["rect_pos"].x + incremento_x
    if nueva_x >= 50 and nueva_x <= 450 - personaje["rect_pos"].width:
        personaje["rect_pos"].x = nueva_x
        pared = False
    return pared

def avanzar_fila(personaje, incremento_y: int, respuesta: bool):
    if (personaje["rect_pos"].x <= 50 or personaje["rect_pos"].x >= 500 - personaje["rect_pos"].width - 10): # Si toca borde
        if respuesta:
            personaje["rect_pos"].x = 50  
            personaje["rect_pos"].y -= incremento_y
        else:
            personaje["rect_pos"].y += incremento_y
