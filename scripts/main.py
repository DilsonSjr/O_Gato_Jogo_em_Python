import pyxel
from jogador import Personagem
from batalha import combate
from menu import menu
from mundo import Mapa
from inimigo import inimigo
fps = 60

class Jogo:

    def __init__(self):

        pyxel.init(192, 108, fps=fps, title="Jogo") # 160x144 pixels sao a resolucao do gameboy
        pyxel.load('../assets/images/bartolomeu.pyxres')  

        
        self.jogador = Personagem(31, 80)
        self.inimigo = inimigo(20,20, self.jogador)
        
        #combate()
        # Mapa(self.jogador).run()

        pyxel.run(self.update, self.draw)

    def update(self):

        self.jogador.mover()
        self.inimigo.detectarjogador()

    def draw(self):
        
        pyxel.cls(1)
        pyxel.bltm(0, 0, 0, 0, 0, 300, 300)
        pyxel.blt(31,90,0,0,248,16,16,0)
        self.inimigo.desenhar()

        self.jogador.desenhar()

# Inicializa o jogo
Jogo()