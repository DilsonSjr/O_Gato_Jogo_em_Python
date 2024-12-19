import pyxel
from jogador import Personagem
from inimigo import Inimigo
from NPC import NPC
from batalha import Combate
class Mapa:
    def __init__(self, jogador):
        pyxel.load('../assets/images/bartolomeu.pyxres')        
        self.jogador = jogador
        self.inimigo = Inimigo(20, 20)
        self.npc = NPC(120, 70, self.jogador)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.mover()
        self.npc.detectar_jogador()

        if self.inimigo.x == self.jogador.x or self.inimigo.y == self.jogador.y:
            Combate(self.jogador, self.inimigo,self)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
        self.inimigo.desenhar()
        self.jogador.desenhar()
        self.npc.desenhar()

    def retornar_ao_mundo(self):
        pyxel.run(self.update, self.draw)