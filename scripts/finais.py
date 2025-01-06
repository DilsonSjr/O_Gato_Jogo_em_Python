import pyxel
import time


class Final:
    def __init__(self, ending_Type, jogador):
        self.jogador = jogador
        self.time =  0

        pyxel.cls(0)
        if ending_Type == "ganhou":
            pyxel.run(self.timer, self.ganhou)
        elif ending_Type == "morreu":
            pyxel.run(self.timer, self.morreu)
        
    def ganhou(self):
        pyxel.cls(0)
        pyxel.text(10 + self.jogador.xCameraOffset, 30 + self.jogador.yCameraOffset, "Voce passa pelo portao dourado, mas \n algo parece muito errado...", 7)
        if self.time > 200:
            pyxel.text(60 + self.jogador.xCameraOffset, 50 + self.jogador.yCameraOffset, "Fim......?", 7)
            pyxel.text(70 + self.jogador.xCameraOffset, 80 + self.jogador.yCameraOffset, "Em breve nos cinemas!", 7)
            pyxel.text(60 + self.jogador.xCameraOffset, 90 + self.jogador.yCameraOffset, "Ou na Steam?", 7)
            pyxel.text(40 + self.jogador.xCameraOffset, 100 + self.jogador.yCameraOffset, "Não sei, mas aqui acabou tchau", 7)
            pyxel.text(60 + self.jogador.xCameraOffset, 120 + self.jogador.yCameraOffset, "Obrigado por jogar!!!", 7)

    def morreu(self):
        pyxel.cls(0)
        pyxel.text(60 + self.jogador.xCameraOffset, 50 + self.jogador.yCameraOffset, "Voce morreu", 7)
        if self.time > 200:
            pyxel.text(60 + self.jogador.xCameraOffset, 90 + self.jogador.yCameraOffset, "Fim......?", 7)
            pyxel.text(30 + self.jogador.xCameraOffset, 100 + self.jogador.yCameraOffset, "Reinicie e tente novamente!\nmiado fraco", 7)

    
    def timer(self):
        self.time += 1