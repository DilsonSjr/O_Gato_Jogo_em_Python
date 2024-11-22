import pyxel

class Player:

    #status jogador
    def __init__(self):
        self.x = 50 
        self.y = 60 
        pyxel.load("D://Documents_SATA//Faculdade//Python//Jogo//assets//images//player.pyxres")
    def update(self):
        #deixando as variaveis do personagem globais
        global velocidade
        global tamanho 
        tamanho = 16
        velocidade = 1
        #correr
        if pyxel.btn(pyxel.KEY_LSHIFT):
            pyxel.load("D:/Documents_SATA/Faculdade/Python/Jogo/assets/images/playerrunning.pyxres")

            velocidade = 3
            #cor = pyxel.COLOR_LIGHT_BLUE
        else:
            velocidade = 0.5
            #cor = pyxel.COLOR_DARK_BLUE
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
        pyxel.blt(self.x, self.y, 0, 0, 0, tamanho,tamanho)