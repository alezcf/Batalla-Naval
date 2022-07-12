import numpy
import pygame, sys
import random
def generar_tablero(nombre):
    archivo = open(nombre, "r")
    ls = []
    for linea in archivo:
        ls.append(linea.strip().split(","))
    tablero = numpy.empty([len(ls),len(ls[0])],type(int))
    for x in range(0, len(ls)):
        for y in range(0, len(ls[0])):
            tablero[x][y] = ls[x][y]    
    return tablero    
pygame.init()
## Resolucion de pantalla
pantalla = pygame.display.set_mode((800,600))
## Generar matrices de vision
tablero_jugador_visible = numpy.empty((10, 10),type(int))
tablero_enemigo_visible = numpy.empty((10, 10),type(int))
## Generar matrices de botes.
numero_documento = random.randint(1, 2)
numero_documento = "tablero" + str(numero_documento) + ".txt"
tablero_jugador_visible = generar_tablero(numero_documento)
tablero_enemigo_visible = generar_tablero(numero_documento)
## Fondo de la pantalla
entorno = pygame.image.load("tablero.png")
## Mostrar por pantalla el fondo
pantalla.blit(entorno, (0, 0))
## Identificacion (Jugador / Computador)
jugador = pygame.image.load("jugador.png")
computador = pygame.image.load("computador.png")
pantalla.blit(jugador, (90, 10))
pantalla.blit(computador, (480, 10))
## Tachar si falla un tiro
acierto = pygame.image.load("fallo.png")
fallo = pygame.image.load("acierto.png")
## Victoria o derrota
victoria = pygame.image.load("victoria.png")
derrota = pygame.image.load("derrota.png")
## Mensaje de acierto o fallo de un tiro.
acierto_tiro = pygame.image.load("boom.png")
fallo_tiro = pygame.image.load("fallaste.png")
## Colores de letras
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
## Test de mouse rectangulo
pygame.draw.rect(pantalla, NEGRO, (800, 600, 200, 200))
## Nombre de la ventana
pygame.display.set_caption("BATALLA NAVAL")
## Estadisticas generales
descubierto_aliado = 0
descubierto_enemigo = 0
espada = pygame.image.load("separacion.png")
pantalla.blit(espada, (390, 15))
## Simbologia
pantalla.blit(acierto, (330, 500))
pantalla.blit(fallo,(330, 540))
## Letras
fuente_letras = pygame.font.SysFont("arial black", 20)
texto = fuente_letras.render("SIMBOLOGIA", True, NEGRO)
pantalla.blit(texto, (330, 460))
texto = fuente_letras.render("Acierto", True, NEGRO)
pantalla.blit(texto, (365, 498))
texto = fuente_letras.render("Fallo", True, NEGRO)
pantalla.blit(texto, (365, 538.5))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if(descubierto_aliado == 20 or descubierto_enemigo == 20):
            continue
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                fila = -1
                columna = -1
                for x in range(1, 11):
                    if(pos[0] > 28 + (31 * x) and pos[0] < 50 + (33 * x ) ):
                        columna = x
                    for y in range(1, 11):
                        if(pos[1] > 35 + (30 * x) and pos[1] < 55 + (31.5 * x )):
                            fila = x
                x_enemigo = random.randint(1, 10)
                y_enemigo = random.randint(1, 10) 
                while(tablero_enemigo_visible[x_enemigo - 1][y_enemigo - 1] == '-'):
                    x_enemigo = random.randint(1, 10)
                    y_enemigo = random.randint(1, 10) 
                if(tablero_jugador_visible[fila - 1][columna - 1] == '-'):
                    continue
                else:
                    if(fila != -1 and columna != -1):
                        if(tablero_jugador_visible[fila - 1][columna - 1] == 'X'):
                            pantalla.blit(acierto, (24 + (31.5 * columna),  48 + (fila * 28)))
                            descubierto_aliado += 1
                            pantalla.blit(acierto_tiro, (100, 390))
                        else:
                            pantalla.blit(fallo, (24 + (31.5 * columna),  48 + (fila * 28)))      
                            pantalla.blit(fallo_tiro, (100, 390))           
                        tablero_jugador_visible[fila - 1][columna - 1] = '-'
                        if(tablero_enemigo_visible[x_enemigo - 1][y_enemigo - 1] == 'X'):
                            pantalla.blit(acierto, (431 + (31.5 * x_enemigo),  48 + (y_enemigo * 28)))
                            descubierto_enemigo += 1
                            pantalla.blit(acierto_tiro, (540, 390))
                        else:
                            pantalla.blit(fallo, (431 + (31.5 * x_enemigo),  48 + (y_enemigo * 28)))
                            pantalla.blit(fallo_tiro, (540, 390))
                        tablero_enemigo_visible[x_enemigo - 1][y_enemigo - 1] = '-'
                if(descubierto_aliado == 20):
                    pantalla.blit(victoria, (200, 100))
                elif(descubierto_enemigo == 20):
                    pantalla.blit(derrota, (200, 100))
    pygame.display.update()