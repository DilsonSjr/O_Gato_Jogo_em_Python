import pyxel
from jogador import Personagem
from inimigo import Inimigo
from batalha import Combate
from NPC import NPC

class Jogo:

    def __init__(self):

        pyxel.init(160, 144, fps = 60, title = "Jogo") # 160x144 pixels sao a resolucao do gameboy
        pyxel.load('../assets/images/bartolomeu.pyxres')

        self.jogador = Personagem(31, 80)
        self.inimigo = Inimigo(20, 20)
        self.npc = NPC(120, 70, self.jogador)

        pyxel.run(self.update, self.draw)

    def update(self):

        self.jogador.mover()
        self.npc.detectar_jogador()

        if self.inimigo.x == self.jogador.x or self.inimigo.y == self.jogador.y:
                Combate(self.jogador, self.inimigo)
        
    def draw(self):
        
        pyxel.cls(1)
        pyxel.bltm(0, 0, 0, 0, 0, 300, 300)
        pyxel.blt(31, 90, 0, 0, 248, 16, 16,0)
        

        self.inimigo.desenhar()
        self.jogador.desenhar()
        self.npc.desenhar()

Jogo()