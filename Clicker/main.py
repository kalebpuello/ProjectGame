import pygame
import constantes
from pelota import Pelota
import time


pygame.init()

#SONIDOS
#música de fondo
pygame.mixer.music.load("assets/sounds/BackgroundSound.mp3")
pygame.mixer.music.play(-1)
#sonido de burbuja
bubble_sound = pygame.mixer.Sound("assets/sounds/burbuja.mp3")


#IMAGENES
#Fondo
fondo = pygame.image.load("assets/Images/BackGround.jpg")
fondo = pygame.transform.scale(fondo, (constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
#Menú
menu_imagen = pygame.image.load("assets/Images/Pantalla_Menu.png")
menu_imagen = pygame.transform.scale(menu_imagen, (constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))


#PANTALLA
screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
pygame.display.set_caption("Clicker")

#FUENTES
font = pygame.font.SysFont(None, 36)
font_grande = pygame.font.SysFont(None, 64)



def dibujar_muros(screen):
    pygame.draw.rect(screen, constantes.BLACK, (0, 0, constantes.SCREEN_WIDTH, 10))
    pygame.draw.rect(screen, constantes.BLACK, (0, 0, 10, constantes.SCREEN_HEIGHT))
    pygame.draw.rect(screen, constantes.BLACK, (constantes.SCREEN_WIDTH - 10, 0, 10, constantes.SCREEN_HEIGHT))
    pygame.draw.rect(screen, constantes.BLACK, (0, constantes.SCREEN_HEIGHT - 10, constantes.SCREEN_WIDTH, 10))

def mostrar_texto(screen, texto, pos):
    label = font.render(texto, True, constantes.BLACK)
    screen.blit(label, pos)


def mostrar_texto_menu(screen, texto, pos,fuente):
    label = fuente.render(texto, True, constantes.BLACK)
    screen.blit(label, pos)

def mostrar_menu():
    running = True
    while running:
        screen.blit(menu_imagen, (0, 0))

        #Botones
        play_button_rect = pygame.Rect(constantes.SCREEN_WIDTH // 2 - 100, constantes.SCREEN_HEIGHT // 2 + 30, 200, 100)
        options_button_rect = pygame.Rect(constantes.SCREEN_WIDTH // 2 - 100, constantes.SCREEN_HEIGHT // 2 + 160, 200, 100)
        mostrar_texto_menu(screen, "Play Game", (play_button_rect.x + 10, play_button_rect.y + 10),font_grande)
        mostrar_texto_menu(screen, "Exit", (options_button_rect.x + 60, options_button_rect.y + 10),font_grande)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    main() #Funcion Principal
                elif options_button_rect.collidepoint(event.pos):
                      pygame.quit()

        pygame.display.flip()


#Alerta para el usuario
def mostrar_alerta_pygame(screen, mensaje):

    texto = font_grande.render(mensaje, True, constantes.RED)
    texto_rect = texto.get_rect(center=(constantes.SCREEN_WIDTH // 2, constantes.SCREEN_HEIGHT // 2))

    screen.fill((255, 255, 255))
    screen.blit(texto, texto_rect)
    pygame.display.flip()

    # Esperar hasta que se presione una tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False
            if event.type == pygame.KEYDOWN:
                esperando = False

#Funcion Principal
def main():
    pelotas = [Pelota() for _ in range(10)]
    running = True
    clock = pygame.time.Clock()

    tiempo_restante = 100
    tiempo_nivel_inicio = time.time()
    puntos = 0

    while running:
        screen.blit(fondo, (0, 0)) #BackGround

        tiempo_transcurrido = time.time() - tiempo_nivel_inicio
        tiempo_restante = max(100 - tiempo_transcurrido, 0)


        if tiempo_restante == 0: #Fin del juego
            mostrar_alerta_pygame(screen, f"¡Fin del Juego! Puntos totales: {puntos}")
            running = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mostrar_menu()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for pelota in pelotas[:]:
                    if pelota.click_detectado(mouse_pos):
                        bubble_sound.play()
                        puntos += 5
            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.name(event.key).upper()
                for pelota in pelotas[:]:
                    if pelota.verificar_tecla(tecla):
                        bubble_sound.play()
                        puntos += 5

        dibujar_muros(screen) #Muros

        #Pelotas
        for pelota in pelotas:
            pelota.mover()
            pelota.actualizar_fragmentos()
            pelota.dibujar(screen)

        puntos_texto = f"PUNTOS:{puntos:02}"
        mostrar_texto(screen, puntos_texto, (constantes.SCREEN_WIDTH - 180, 10))

        minutos = int(tiempo_restante) // 60
        segundos = int(tiempo_restante) % 60
        tiempo_texto = f"{minutos}:{segundos:02}"
        mostrar_texto(screen, tiempo_texto, (constantes.SCREEN_WIDTH // 2 - 30, 10))

        pygame.display.flip()
        clock.tick(constantes.FPS)

        pelotas = [pelota for pelota in pelotas if pelota.fragmentos or not pelota.fragmentos]

        if not pelotas:
            tiempo_nivel_inicio = time.time() + tiempo_restante
            pelotas = [Pelota() for _ in range(10)]

    pygame.quit()

if __name__ == "__main__":
    mostrar_menu()
