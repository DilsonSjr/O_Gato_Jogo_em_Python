import pyxel
import time
from jogador import Personagem

class NPC:
    def __init__(self, x, y, jogador):
        self.x = x
        self.y = y
        self.jogador = jogador
        self.dialogo = False
        self.tempoInicioDialogo = 0

    def detectar_jogador(self):
        # Verifica se o jogador está próximo ao NPC
        distancia_x = abs(self.x - self.jogador.x)
        distancia_y = abs(self.y - self.jogador.y)
        distancia_maxima = 16  # Distância máxima para interação

        if distancia_x <= distancia_maxima and distancia_y <= distancia_maxima:
            # Verifica se a tecla E está sendo pressionada
            if self.jogador.estado == "interagir" :
                self.dialogo = True
                self.tempoInicioDialogo = time.time()
    def desenhar(self):
        pyxel.blt(self.x, self.y, 0, 0, 176, 16, 16, 0)

        if self.dialogo == True:
            pyxel.rect(self.x -10, self.y -10, 38, 10, 0)
            pyxel.text(self.x -9    , self.y -7,"iae Tchum", 7)

            if time.time() - self.tempoInicioDialogo >= 3:
                    self.dialogo = False