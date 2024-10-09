import pygame
import random
import time
from fragmento import Fragmento
import constantes

class Pelota:
    letras_disponibles = ["A","B","C","D","F","G"]

    def __init__(self):
        self.radius = random.randint(15, 30)
        self.x = constantes.SCREEN_WIDTH // 2
        self.y = constantes.SCREEN_HEIGHT // 2
        self.vel_x = random.uniform(-3, 3)
        self.vel_y = random.uniform(-3, 3)
        self.color = random.choice(constantes.COLORES)
        self.fragmentos = []
        self.tiempo_de_fragmentacion = None

        # Determinar si la pelota es clickeable o necesita una tecla
        self.es_tecla = random.choice([True, False])
        if self.es_tecla and Pelota.letras_disponibles:
            self.tecla_asignada = Pelota.letras_disponibles.pop(random.randint(0, len(Pelota.letras_disponibles) - 1))
        else:
            self.tecla_asignada = None

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x - self.radius <= 10 or self.x + self.radius >= constantes.SCREEN_WIDTH - 10:
            self.vel_x = -self.vel_x
        if self.y - self.radius <= 10 or self.y + self.radius >= constantes.SCREEN_HEIGHT - 10:
            self.vel_y = -self.vel_y

    def dibujar(self, screen):
        if not self.fragmentos:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

            if self.es_tecla:
                font = pygame.font.SysFont(None, 36)
                letra = font.render(self.tecla_asignada, True, constantes.BLACK)
                screen.blit(letra, (int(self.x) - 10, int(self.y) - 10))
        else:
            for fragmento in self.fragmentos:
                fragmento.dibujar(screen)

    def click_detectado(self, mouse_pos):
        if not self.es_tecla:
            distancia = ((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2) ** 0.5
            if distancia <= self.radius:
                self.generar_fragmentos()
                return True
        return False

    def verificar_tecla(self, tecla):
        if self.es_tecla and tecla == self.tecla_asignada:
            self.generar_fragmentos()
            return True
        return False

    def generar_fragmentos(self):
        num_fragmentos = random.randint(5, 10)
        for _ in range(num_fragmentos):
            self.fragmentos.append(Fragmento(self.x, self.y, self.radius // 2, self.color))
        self.tiempo_de_fragmentacion = time.time()

    def actualizar_fragmentos(self):
        if self.fragmentos:
            tiempo_actual = time.time()
            if tiempo_actual - self.tiempo_de_fragmentacion > 3:
                self.fragmentos.clear()
            else:
                for fragmento in self.fragmentos:
                    fragmento.mover()
