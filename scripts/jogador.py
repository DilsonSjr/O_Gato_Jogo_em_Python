import pyxel
from batalha import combate
class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y):
        # Inicializa o personagem
        self.x = x
        self.y = y
        self.velocidade = 1
        
        self.vida = 5
        self.dano = 1

        self.largura = 16  # Dimensão fixa para largura
        self.altura = 16   # Dimensão fixa para altura

        self.estado = "parado"  # Estado atual do personagem
        self.direcao = "direita"  # Direção inicial

        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X na imagem para desenhar o quadro correspondente

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

            # para testar o combate aperta Y (tecla para teste no futuro sera de outra forma para iniciar o combate)
        if pyxel.btn(pyxel.KEY_Y):  # Move para a esquerda
            combate()
                    
    def desenhar(self):
        if self.estado == "parado":
            # Determina o tamanho do sprite com base na direção
            if self.direcao == "direita":
                self.tamanhoSprite = 16
            # elif self.direcao == "esquerda":
            #     self.tamanhoSprite = -16  # Sprite espelhado para esquerda

            # Avança para o próximo quadro da animação
            self.frame += 16 
            if self.frame > 100:  # Reseta ao completar a animação
                self.frame = 0
                self.posU = 0
            
            # Desenha o quadro atual do personagem
            if self.direcao == "direita":
                pyxel.blt(self.x, self.y, 0, self.frame, 0, self.tamanhoSprite, self.tamanhoSprite, 0)
            elif self.direcao == "esquerda":
                pyxel.blt(self.x, self.y, 0, self.frame, 0, -self.tamanhoSprite, self.tamanhoSprite, 0)