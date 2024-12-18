import pyxel

class Inimigo:

    def __init__ (self, x, y):
        d6 = pyxel.rndi(1, 6)
        
        self.x = x
        self.y = y

        self.vida = d6 + 5
        self.dano = 1
        self.xp = d6
        self.estado = "parado"
        self.xTamanhoSprite = 16
        self.yTamanhoSprite = 16
        
        self.frame = 0
        self.contador_animacao = 50 

    def atualizar_d6(self):
        d6 = pyxel.rndi(1, 6)
        self.dano = d6    

    def desenhar(self):

        if self.estado == "parado":
            self.contador_animacao += 1

            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0

            if self.frame > 48:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 160, self.xTamanhoSprite, self.yTamanhoSprite, 0)