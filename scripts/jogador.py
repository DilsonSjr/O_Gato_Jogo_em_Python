import pyxel
import random




class Personagem:
    

    def __init__(self, x, y):
        # Inicializa o personagem
        pyxel.load('../assets/images/BARTOLOMEU.pyxres')  # Carrega a imagem do personagem
        #pyxel.images[0].load(0, 0, '../assets/images/BARTOLOMEU.pyxres')  # Sprites com dimensões uniformes
        
        d6 = random.randint(1, 6)

        self.x = x
        self.y = y
        self.velocidade = 0.1
        
        self.vida = d6 + 5
        self.dano = d6 

        self.largura = 16  # Dimensão fixa para largura
        self.altura = 16   # Dimensão fixa para altura

        self.estado = "parado"  # Estado atual do personagem
        self.direcao = "direita"  # Direção inicial

        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X na imagem para desenhar o quadro correspondente
        self.contador_animacao = 50  # Contador para controlar a velocidade da animação

    def mover(self):

        if pyxel.btn(pyxel.KEY_LSHIFT):  # Move para a esquerda
            self.velocidade = 4
        else:
            self.velocidade = 2

        if pyxel.btn(pyxel.KEY_A):  # Move para a esquerda
            self.direcao = "esquerda"
            self.x -= self.velocidade % 4
        elif pyxel.btn(pyxel.KEY_D):  # Move para a direita
            self.direcao = "direita"
            self.x += self.velocidade % 4
        elif pyxel.btn(pyxel.KEY_W):  # Move para a cima
            #self.direcao = "cima"
            self.y -= self.velocidade % 4
        elif pyxel.btn(pyxel.KEY_S):  # Move para a baixo
            #self.direcao = "baixo"
            self.y += self.velocidade % 4
            
        elif pyxel.btn(pyxel.KEY_E): #botao pra testar a vida e perder 1 de vida
            self.vida = self.vida - 1 

    def desenhar(self):
        pyxel.rect(20, 10, self.vida,5 , 8) # desenha a barra de vida do
        pyxel.text(10, 10, "{}".format(self.vida), 8)
        # voce morreu
        if self.vida <= 0:
            pyxel.text(50, 50, "Voce morreu", 8)
        
        if self.estado == "parado":
            # Determina o tamanho do sprite com base na direção
            if self.direcao == "direita":
                self.tamanhoSprite = 16
            # Incrementa o contador de animação
            # Atualiza o quadro da animação a cada 10 frames
            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0
            # elif self.direcao == "esquerda":

            # Incrementa o contador de animação
            self.contador_animacao += 1
            
            # Atualiza o quadro da animação a cada 10 frames
            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0
            
            if self.frame > 100:  # Reseta ao completar a animação
                self.frame = 0
                self.posU = 0
            
            # Desenha o quadro atual do personagem
            if self.direcao == "direita":
                pyxel.blt(self.x, self.y, 0, self.frame, 0, self.tamanhoSprite, self.tamanhoSprite, 0)
            elif self.direcao == "esquerda":
                pyxel.blt(self.x, self.y, 0, self.frame, 0, -self.tamanhoSprite, self.tamanhoSprite, 0)
