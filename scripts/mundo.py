import pyxel
from jogador import Personagem
from inimigo import Inimigo
from NPC import NPC
from batalha import Combate
class Mapa:
    def __init__(self, jogador):
        pyxel.load('../assets/images/bartolomeu.pyxres')   
        pyxel.playm(00, 1, True) # toca a musica de fundo, 00 é o numero da soundtrack, 1 é os ticks 1 =160, True é se loopa
        self.jogador = jogador
        self.inimigo = Inimigo(200, 420)
        self.npc = NPC(17, 57, self.jogador)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.mover()
        self.npc.detectar_jogador()

        # Verifica se as posições do jogador e do inimigo coincide
        if self.jogador.x == self.inimigo.x and self.jogador.y in range(self.inimigo.y - 50, self.inimigo.y + 50) or self.jogador.y == self.inimigo.y and self.jogador.x in range(self.inimigo.x - 50, self.inimigo.x + 50):
        # if self.jogador.x in range(self.inimigo.x - 50, self.inimigo.x + 50) and self.jogador.y in range(self.inimigo.y - 50, self.inimigo.y + 50):

        # Inicia o combate
            Combate(self.jogador, self.inimigo, self)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 1024, 1024)
        self.inimigo.desenhar()
        self.jogador.desenhar()
        self.npc.desenhar()

    def retornar_ao_mundo(self):
        pyxel.run(self.update, self.draw)