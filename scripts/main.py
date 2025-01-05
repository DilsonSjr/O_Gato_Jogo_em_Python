import pyxel
from menu import Menu

class Jogo:
    def __init__(self):
        pyxel.init(160, 144, fps=60, title="O Gato")  # 160x144 pixels são a resolução do Gameboy
        Menu(xCameraOffset=0, yCameraOffset=0)

Jogo()      

