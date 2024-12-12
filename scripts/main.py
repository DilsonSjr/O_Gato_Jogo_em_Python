import pyxel
from jogador import Personagem
from batalha import combate
from menu import menu
from mundo import Mapa
from inimigo import inimigo
fps = 60

class Jogo:

    def __init__(self):

        pyxel.init(192, 108, fps=fps, title="Jogo")
        pyxel.load('../assets/images/bartolomeu.pyxres')  

        
        self.jogador = Personagem(70, 50)
        self.inimigo = inimigo(20,20, self.jogador)
        combate()
        # Mapa(self.jogador).run()

        pyxel.run(self.update, self.draw)

    def update(self):

        self.jogador.mover()
        self.inimigo.detectarjogador()

    def draw(self):
        
        pyxel.cls(12)
        
        self.inimigo.desenhar()

        self.jogador.desenhar()

# Inicializa o jogo
Jogo()