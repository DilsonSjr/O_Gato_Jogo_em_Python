import pyxel
import time
class Personagem:

    def __init__(self, x, y):
        d6 = pyxel.rndi(1, 6)

        self.x = x 
        self.y = y 
        self.velocidade = 1

        self.vida = d6 + 5
        self.dano = d6 

        self.largura = 16  
        self.altura = 16   

        self.estado = 'parado'  
        self.direcao = 'direita'  
        self.xTamanhoSprite = 16
        self.yTamanhoSprite = 16

        self.frame = 0
        self.contador_animacao = 50  

    def atualizar_d6(self):
        d6 = pyxel.rndi(1, 6)

        self.dano = d6
############ MOVIMENTO ############
    def mover(self):

############ CORRER ############

        if pyxel.btn(pyxel.KEY_LSHIFT):  
            self.velocidade = 1.5
        else:
            self.velocidade = 1


############ BOTOES DO JOGO ############

        if pyxel.btn(pyxel.KEY_A):  # Move para a esquerda
            self.direcao = 'esquerda'
            self.estado = 'andando'
            self.x -= self.velocidade
            self.xTamanhoSprite =  - abs(self.xTamanhoSprite)
        if pyxel.btn(pyxel.KEY_D):  # Move para a direita
            self.direcao = 'direita'
            self.estado = 'andando'
            self.x += self.velocidade
            self.xTamanhoSprite =  abs(self.xTamanhoSprite)
        if pyxel.btn(pyxel.KEY_W):  # Move para a cima
            self.direcao = 'cima'
            self.estado = 'andando'
            self.y -= self.velocidade
        if pyxel.btn(pyxel.KEY_S):  # Move para a baixo
            self.direcao = 'baixo'
            self.estado = 'andando'
            self.y += self.velocidade

        # Detecta quando as teclas de movimento são liberadas
        if pyxel.btnr(pyxel.KEY_A) or pyxel.btnr(pyxel.KEY_D) or pyxel.btnr(pyxel.KEY_W) or pyxel.btnr(pyxel.KEY_S):
            self.estado = 'parado'

############ INTERAGIR ############
        if pyxel.btn(pyxel.KEY_E):
            self.estado = 'interagir'  # Botão de interação
############ TESTAR - VIDA ############
        if pyxel.btn(pyxel.KEY_V): #botao pra testar a vida e perder 1 de vida
            self.vida = self.vida - 1 


############ UPDATE ############
    def update(self):
        self.jogador.mover()
############ DRAW ############
    def desenhar(self):
        pyxel.camera(self.x - pyxel.width // 2 +10, self.y - pyxel.height // 2 +10)
        pyxel.rect(self.x -81,self.y - 49, self.vida, 5, 0)  
        pyxel.rect(self.x -80,self.y - 50, self.vida, 5, 8)  #Desenha a barra de vida do jogador

############ DESENHA BARRA DE VIDA DO JOGADOR ############
        pyxel.text(self.x - 91,self.y - 49, "{}".format(self.vida), 0)
        pyxel.text(self.x - 90,self.y - 50, "{}".format(self.vida), 8)

############ DEFINE MORTE ############
        if self.vida <= 0:
            pyxel.text(self.x -15, self.y - 10, "Voce morreu", 8)

############ ANIMAÇÕES ############
        if self.estado == "parado":
            self.contador_animacao += 1

            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0

            if self.frame > 48:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 0, self.xTamanhoSprite, self.yTamanhoSprite, 0)

        if self.estado == 'andando':
            self.contador_animacao += 1

            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0

            if self.frame > 96:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 64, self.xTamanhoSprite, self.yTamanhoSprite, 0)

        if self.estado == 'interagir':
            self.contador_animacao += 1 

            if self.contador_animacao >= 10:
                self.frame += 16 
                self.contador_animacao = 0 

            if self.frame > 96-16:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 112, self.xTamanhoSprite, self.yTamanhoSprite, 0)
            if self.frame == 96-16:
                self.estado = "parado"