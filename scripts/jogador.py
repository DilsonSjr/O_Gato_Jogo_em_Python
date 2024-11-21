import pyxel

class Player:

    #status jogador
    def __init__(self):
        self.x = 50 
        self.y = 60 

    def update(self):
        #deixando as variaveis do personagem globais
        global velocidade
        global cor
        global tamanho
        #correr
        if pyxel.btn(pyxel.KEY_LSHIFT):
            velocidade = 1
            cor = pyxel.COLOR_LIGHT_BLUE
            tamanho = 4
        else:
            velocidade = 0.5
            cor = pyxel.COLOR_DARK_BLUE
            tamanho = 8
        #andar do jgodaor
        if pyxel.btn(pyxel.KEY_A):
            self.x -= velocidade
        if pyxel.btn(pyxel.KEY_D):
            self.x += velocidade
        if pyxel.btn(pyxel.KEY_W):
            self.y -= velocidade
        if pyxel.btn(pyxel.KEY_S):
            self.y += velocidade
    #circulo do jogador (temporario)
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, tamanho,cor)