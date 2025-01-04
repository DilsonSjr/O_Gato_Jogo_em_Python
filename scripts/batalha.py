import pyxel
import random

class Combate:
    def __init__(self, jogador, inimigo, mundo):
        self.jogador = jogador
        self.inimigo = inimigo
        self.mundo = mundo
        self.combate_ativo = True
        self.resultado = None
        self.turno = 0
        self.rodada = 0
        self.opcaoSelecionada = 0
        self.opcoes = ["Atacar", "Descansar", "Fugir"]
        self.last_turn_heal = False

        ############ DEBUG DO COMBATE ############
        print("dano ", self.jogador.dano)
        print("vida ", self.jogador.vida)
        print("inimigo dano ", self.inimigo.dano)
        print("inimigo vida ", self.inimigo.vida)

        ############ TEXTOS DO COMBATE ############
        self.TextosDeAtaque = self.inimigo.texto

        self.frame_count = 0  # Contador de quadros para controlar o tempo de introdução

        pyxel.run(self.update, self.draw)

    def verificarEstadoCombate(self):
        if self.inimigo.vida <= 0:
            self.resultado = "vitoria"
            self.combate_ativo = False
        elif self.jogador.vida <= 0:
            self.resultado = "derrota"
            self.combate_ativo = False

    def acoes(self):
        if self.opcoes[self.opcaoSelecionada] == "Atacar":
            pyxel.text(10 + self.jogador.xCameraOffset, 15 + self.jogador.yCameraOffset, "Atacou", 7)
            self.inimigo.vida = self.inimigo.vida - self.jogador.dano
            self.last_turn_heal = False
        elif self.opcoes[self.opcaoSelecionada] == "Recuperar" and not self.last_turn_heal:
            pyxel.text(10 + self.jogador.xCameraOffset, 15 + self.jogador.yCameraOffset, "Recuperou", 7)
            self.jogador.vida += self.jogador.dano
            self.last_turn_heal = True
        elif self.opcoes[self.opcaoSelecionada] == "Fugir":
            pyxel.text(10 + self.jogador.xCameraOffset, 15 + self.jogador.yCameraOffset, "Você fugiu do combate!", 7)
            self.jogador.estado = 'parado'
            self.inimigo.time = 100
            self.mundo.retornar_ao_mundo()

    ############ ATUALIZAÇÃO DO COMBATE ############
    def update(self):
        if self.frame_count < 90:  # Contador para os primeiros 3 segundos
            self.frame_count += 1  # Incrementa o contador
            return  # Nada mais é atualizado enquanto na introdução

        if not self.combate_ativo:
            return

        self.verificarEstadoCombate()

        if not self.combate_ativo:
            if self.resultado == "vitoria":
                pyxel.text(10 + self.jogador.xCameraOffset, 15 + self.jogador.yCameraOffset, "Você venceu o combate!", 8)
                self.inimigo.time = 100
                self.jogador.estado = 'parado'
                self.jogador.xp = self.jogador.xp + self.inimigo.xp
                self.jogador.vida += 5
                self.mundo.retornar_ao_mundo()
                return
            elif self.resultado == "derrota":
                self.inimigo.time = 100
                self.jogador.estado = 'parado'
                pyxel.text(10 + self.jogador.xCameraOffset, 15 + self.jogador.yCameraOffset, "Você perdeu o combate!", 8)
                self.mundo.retornar_ao_mundo()
                return

        if self.turno == 0:
            if pyxel.btnp(pyxel.KEY_A):
                self.opcaoSelecionada = (self.opcaoSelecionada - 1) % len(self.opcoes)
            elif pyxel.btnp(pyxel.KEY_D):
                self.opcaoSelecionada = (self.opcaoSelecionada + 1) % len(self.opcoes)
            elif pyxel.btnp(pyxel.KEY_SPACE):
                self.acoes()
                self.turno = 1
                self.rodada += 1

        elif self.turno == 1:
            acao = random.choice(["ataque", "ataque", "ataque", "ataque", "recupere"])
            if acao == "ataque":
                self.jogador.vida = self.jogador.vida - self.inimigo.dano
            elif acao == "recupere":
                self.inimigo.vida = self.inimigo.vida + self.inimigo.dano
            self.turno = 0

############ DESENHO DO COMBATE INICIADO ############
    def draw(self):
############ ANIMACAO DO COMBATE INICIANDO ############
        if  self.frame_count < 90:
            pyxel.rect(0 + self.jogador.xCameraOffset, 0 + self.jogador.yCameraOffset, 160, 36, 0)
            pyxel.rect(0 + self.jogador.xCameraOffset, 120 + self.jogador.yCameraOffset, 160, 36, 0)
            pyxel.text(10 + self.jogador.xCameraOffset, 10 + self.jogador.yCameraOffset, self.TextosDeAtaque, 7)
############ MENU DE COMBATE ############
        else:
            pyxel.cls(1)
            pyxel.blt(0 + self.jogador.xCameraOffset, -64 + self.jogador.yCameraOffset, 1, 0, 0, 192, 192)
            pyxel.rect(0 + self.jogador.xCameraOffset, 0 + self.jogador.yCameraOffset, 160, 48, 0)
            pyxel.blt(50 + self.jogador.xCameraOffset, 50 + self.jogador.yCameraOffset, 1, 0, 0, 64, 64, 0)  # sprite do inimigo
            pyxel.rect(0 + self.jogador.xCameraOffset, 100 + self.jogador.yCameraOffset, 160, 48, 0)
            pyxel.text(10 + self.jogador.xCameraOffset, 5 + self.jogador.yCameraOffset, f"Rodada: {self.rodada}", 7)
            
############ OPCOES DE COMBATE ############
            for i, opcao in enumerate(self.opcoes):
                cor = 7 if i == self.opcaoSelecionada else 6
                pyxel.text(10 + i * 40 + self.jogador.xCameraOffset, 120 + self.jogador.yCameraOffset, opcao, cor)
############ desenha a barra de vida do jogador ###########
            pyxel.rect(20 + self.jogador.xCameraOffset, 110 + self.jogador.yCameraOffset, self.jogador.vida, 5, 11)
            pyxel.text(10 + self.jogador.xCameraOffset, 110 + self.jogador.yCameraOffset, "{}".format(self.jogador.vida), 11)
            
############ desenha a barra de vida do inimigo ############
            pyxel.rect(80 + self.jogador.xCameraOffset, 22 + self.jogador.yCameraOffset, self.inimigo.vida, 5, 8)