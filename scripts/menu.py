import pyxel
from mundo import Mapa
from batalha import Combate
from jogador import Personagem
from inimigo import Inimigo

class Menu:
    def __init__(self, xCameraOffset, yCameraOffset):
        pyxel.load('../assets/images/bartolomeu.pyxres')
        self.opcoes = ["Jogar", "Batalhar", "Créditos", "Fechar"]
        self.opcao_selecionada = 0
        self.ativo = True

        self.xCameraOffset = xCameraOffset 
        self.yCameraOffset = yCameraOffset

        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.ativo:
            return
        
        if pyxel.btnp(pyxel.KEY_W):
            self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_S):
            self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.executar_acao()

    def draw(self):
        pyxel.cls(1)
        pyxel.blt(0 + self.xCameraOffset, -64 + self.yCameraOffset, 1, 0, 0, 192, 192)
        pyxel.rect(0 + self.xCameraOffset, 100 + self.yCameraOffset, 160, 56, 0)
        for i, opcao in enumerate(self.opcoes):
            cor = 10 if i == self.opcao_selecionada else 9
            pyxel.text(self.xCameraOffset + 10, self.yCameraOffset + 105 + i * 10, opcao, cor)

    def executar_acao(self):
        if self.opcao_selecionada == 0:
            self.Jogar()
        elif self.opcao_selecionada == 1:
            self.Batalhar()
        elif self.opcao_selecionada == 2:
            self.Creditos()
        elif self.opcao_selecionada == 3:
            self.Fechar()

    def Jogar(self):
        Mapa(Personagem(31, 80))  # Substitua 31, 80 pela posição inicial desejada

    def Batalhar(self):
        jogador = Personagem(80, 60)  # Substitua 80, 60 pela posição inicial desejada
        inimigo = Inimigo(100, 60)  # Substitua 100, 60 pela posição inicial desejada
        Combate(jogador=jogador, inimigo=inimigo)

    def Creditos(self):
        return

    def Fechar(self):
        pyxel.close()