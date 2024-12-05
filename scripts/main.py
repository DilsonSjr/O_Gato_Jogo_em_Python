import pyxel
from jogador import Personagem

fps = 6
imagem_jogador = 'D:/Documents_SATA/Faculdade/Python/Jogo/assets/images/BARTOLOMEU.png'

class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa a janela e carrega os recursos
        pyxel.init(160, 120, fps=fps, title="Animações")  # Tela de 160x120, 10 FPS
        pyxel.images[0].load(0, 0, imagem_jogador)  # Sprites com dimensões uniformes
        
        # Cria o personagem no jogo
        self.jogador = Personagem(70, 50)

        # Inicia o loop principal do jogo
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo
        self.jogador.mover()

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(12)  # Limpa a tela com a cor de fundo
        self.jogador.desenhar()

# Inicializa o jogo
Jogo()