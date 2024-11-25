import pyxel
from jogador import Player

class itensdomundo:
    parede = (0,1)
    chao = (0,0)
    Player = (1, 1)

class mundo:
    altura = 16
    largura = 16

    def __init__(self,tilemap):
        self.tilemap = tilemap
        self.mundo_map = []
        self.player_grid_x = 0
        self.player_grid_y = 0
        for y in range(self.altura):
            if self.tilemap_pget(x,y) == itensdomundo.parede:
                self.mundo_map[y].append(itensdomundo.parede)
            elif self.tilemap_pget(x,y) == itensdomundo.Player:
                self.mundo_map[y].append(itensdomundo.chao)
                self.player_grid_x = x
                self.player_grid_y = y
            else:
                self.mundo_map[y].append(itensdomundo.chao)