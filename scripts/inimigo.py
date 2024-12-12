import pyxel
import random
from jogador import Personagem

class inimigo:

    def __init__ (self, x, y,Personagem):
        self.jogador = Personagem

        d6 = random.randint(1,6)
        self.x = x
        self.y = y


        self.frame = 0
        self.altura = 16
        self.largura = 16
        self.estado = "parado"
        self.frame = 0  # Controla o quadro atual da animação
        self.contador_animacao = 50  # Contador para controlar a velocidade da animação   

######## Atributos do inimigo 

        self.vida = d6 * 5
        self.dano = d6


    
    def atualizar_d6(self):
        d6 = random.randint(1,6)
        self.dano = d6    

    def detectarjogador(self):
        if self.x == self.jogador .x or self.y == self.jogador.y:
            print ("colidiu")

    def desenhar(self):

        if self.estado == "parado":
            self.contador_animacao += 1

            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0

        if self.frame > 100:
                self.frame = 0
        
        #pyxel.rect(self.x, self.y, self.altura, self.altura, 2)
        pyxel.blt(self.x, self.y, 0,self.frame, 160, self.altura, self.largura, 0)