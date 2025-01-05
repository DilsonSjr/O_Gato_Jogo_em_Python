import pyxel

class Inimigo:

    def __init__ (self, x, y, vida, dano, sprite_x, sprite_y, texto):     
        self.x = x
        self.y = y
        
        self.texto = texto
        self.vida = vida
        self.dano = dano
        self.xp = pyxel.rndi(1, 6)
        self.estado = "parado"
        self.xTamanhoSprite = 16
        self.yTamanhoSprite = 16
        
        self.frame = 0
        self.contador_animacao = 50 
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y

        self.time = 0    

    def desenhar(self):
        
        if self.time > 0:
            self.time -= 1

        if self.estado == "parado":
            self.contador_animacao += 1

            if self.contador_animacao >= 10:
                self.frame += 16
                self.contador_animacao = 0

            if self.frame > 48:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.sprite_x + self.frame, self.sprite_y, self.xTamanhoSprite, self.yTamanhoSprite, 0)