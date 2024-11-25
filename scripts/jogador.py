import pyxel
tamanho = 16
velocidade = 1
class Player:

    #status jogador
    def __init__(self):
        self.x = 50 
        self.y = 60 
        pyxel.load("D://Documents_SATA//Faculdade//Python//Jogo//assets/images//texture.pyxres")
    def update(self):
        #deixando as variaveis do personagem globais

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
        pyxel.blt(self.x, self.y, 0, 16, 0, tamanho,tamanho)