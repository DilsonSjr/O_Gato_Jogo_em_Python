import pyxel
import random

class Personagem:

    def __init__(self, x, y):
        d6 = random.randint(1, 6)

        self.x = x
        self.y = y
        self.velocidade = 0.1

        self.vida = d6 + 5
        self.dano = d6 

        self.largura = 16  # Dimensão fixa para largura
        self.altura = 16   # Dimensão fixa para altura

        self.estado = 'parado'  # Estado atual do personagem
        self.direcao = 'direita'  # Direção inicial
        self.xTamanhoSprite = 16
        self.yTamanhoSprite = 16

        self.frame = 0  # Controla o quadro atual da animação
        self.contador_animacao = 50  # Contador para controlar a velocidade da animação

    def atualizar_d6(self):
        d6 = random.randint(1, 6)

        self.dano = d6

    def mover(self):

        if pyxel.btn(pyxel.KEY_LSHIFT):  # Move para a esquerda
            self.velocidade = 1.5
        else:
            self.velocidade = 1

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

        # if pyxel.btnr(not(pyxel.btns())):
        #     self.estado = 'parado'

        if pyxel.btn(pyxel.KEY_E): #botao pra testar a vida e perder 1 de vida
            self.vida = self.vida - 1 

    def update(self):
        self.jogador.mover()

    def desenhar(self):
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        pyxel.rect(self.x -49,self.y - 49, self.vida, 5, 0)  
        pyxel.rect(self.x -50,self.y - 50, self.vida, 5, 8)  #Desenha a barra de vida do jogador
#Desenha a barra de vida do jogador
        pyxel.text(self.x -59,self.y - 49, "{}".format(self.vida), 0)
        pyxel.text(self.x -60,self.y - 50, "{}".format(self.vida), 8)

        if self.vida <= 0:
            pyxel.text(self.x -15, self.y - 10, "Voce morreu", 8)

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