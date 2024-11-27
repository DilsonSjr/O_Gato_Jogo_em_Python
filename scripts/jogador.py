import pyxel

class Player:

    def __init__(self):
        
        self.x = 50 
        self.y = 60 
        self.velocidade = 0
        #carrega a imagem
        self.vida = 5
        self.dano = 1
        pyxel.load('D://Documents_SATA//Faculdade//Python//Jogo//assets\sounds//texture.pyxres')
        self.imagem = pyxel.images[0].load(0, 0, 'D://Documents_SATA//Faculdade//Python//Jogo//assets\sounds//texture.pyxres')
        self.estado = 'direita'
        self.quadro = 1
        self.direita = [0,0,0,16]
        self.esquerda = [0,0,0,16]
        self.cima = [0,0,0,16]
        self.baixo = [0,0,0,16]
        self.tamanho = 16

    def update(self):
        
        if pyxel.btn(pyxel.KEY_A):
            self.estado = 'esquerda'
            self.x -= self.velocidade
            self.quadro = (self.quadro + 1) % 4
        if pyxel.btn(pyxel.KEY_D):
            self.estado = 'direita'
            self.x += self.velocidade
            self.quadro = (self.quadro + 1) % 4
        if pyxel.btn(pyxel.KEY_W):
            self.estado = 'cima'
            self.y -= self.velocidade
            self.quadro = (self.quadro + 1) % 4
        if pyxel.btn(pyxel.KEY_S):
            self.estado = 'baixo'
            self.y += self.velocidade
            self.quadro = (self.quadro + 1) % 4

        if pyxel.btn(pyxel.KEY_LSHIFT):
            self.velocidade = 1
            self.tamanho = 16
        else:
            self.velocidade = 0.5
            self.tamanho = 16
    
    def draw(self):
        # Define o quadro do sprite do gato
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 16,16, 2)
        if self.estado == 'direita':
            pyxel.blt(self.x, self.y, 0, self.direita[self.quadro], 16, self.tamanho,  self.tamanho, 0)
        elif self.estado == 'esquerda':
            pyxel.blt(self.x, self.y, 0, self.esquerda[self.quadro], 16,  self.tamanho,  self.tamanho, 0)
        elif self.estado == 'cima':
            pyxel.blt(self.x, self.y, 0, self.cima[self.quadro], 16,  self.tamanho,  self.tamanho, 0)
        elif self.estado == 'baixo':
            pyxel.blt(self.x, self.y, 0, self.baixo[self.quadro], 16,  self.tamanho,  self.tamanho, 0)