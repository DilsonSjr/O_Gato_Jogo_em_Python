import pyxel

class Mapa():
    def __init__(self, Player):
        self.jogador = Player
        
        self.hitboxes = [
            (10, 10, 16, 16),  # (x, y, largura, altura)
            (50, 50, 32, 32),
        ]

    def colide(self, rect1, rect2):
        return (rect1[0] < rect2[0] + rect2[2] and
                rect1[0] + rect1[2] > rect2[0] and
                rect1[1] < rect2[1] + rect2[3] and
                rect1[1] + rect1[3] > rect2[1])

    def update(self):
        player_rect = (self.jogador.x, self.jogador.y, 16, 16)

        for hitbox in self.hitboxes:
            if self.colide(player_rect, hitbox):
                print("Colidiu!")

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 160, 120)
        
        # Draw the hitboxes for debug
        for hitbox in self.hitboxes:
            pyxel.rect(hitbox[0], hitbox[1], hitbox[2], hitbox[3], 8)

    def run(self):
        pyxel.run(self.update, self.draw)