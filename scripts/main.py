import pyxel
from jogador import Player

class App:
    def __init__(self):
        pyxel.init(160, 120, title="O jogo", fps=60)
        self.jogador = Player() 
        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.update() 

    def draw(self):
        pyxel.cls(0)
        self.jogador.draw() 

App()