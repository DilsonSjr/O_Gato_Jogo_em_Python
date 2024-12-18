import pyxel
import random
import time

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
        self.opcoes = ["Atacar", "Especial", "Itens", "Fugir"]

        self.inimigo.xp   = self.inimigo.xp
        self.jogador.xp   = self.jogador.xp
        self.jogador.vida = self.jogador.vida
        self.jogador.dano = self.jogador.dano
        self.inimigo.vida = self.inimigo.vida

        self.xCameraOffset = self.jogador.xCameraOffset
        self.yCameraOffset = self.jogador.yCameraOffset

        ############ DEBUG DO COMBATE ############
        print("dano ", self.jogador.dano)
        print("vida ", self.jogador.vida)
        print("inimigo dano ", self.inimigo.dano)
        print("inimigo vida ", self.inimigo.vida)

        ############ TEXTOS DO COMBATE ############
        self.TextosDeAtaque = random.choice([
            "Prepare-se para sentir minhas garras,\ninvasor!",
            "Voce ousa entrar no meu territorio?\nVai pagar por isso!",
            "Hora de mostrar quem e o verdadeiro\nrei deste quintal!",
            "Minhas patas nao falham!\nVenha se atrever!",
            "Voce acabou de arranjar uma briga\nque nao pode vencer, miado fraco!",
            "Eu estava so cochilando, mas agora\nvou te ensinar uma licao!",
            "Prepare-se para um verdadeiro\nduelo felino!",
            "Suas chances sao tao boas quanto um rato\nno meio de uma colonia de gatos!",
            "Voce e corajoso, mas nao sera pario\npara minhas presas afiadas!",
            "Miau, miau... Hora de lutar ate\no ultimo pelo!"
        ])

        self.tempoInicio = time.time()

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
            print("Jogador escolheu atacar")
            pyxel.text(50, 10, "Atacou", 7)
            self.inimigo.vida = self.inimigo.vida - self.jogador.dano

        elif self.opcoes[self.opcaoSelecionada] == "Especial":
            print("Jogador escolheu especial")
            # fazer logica de especial
        elif self.opcoes[self.opcaoSelecionada] == "Itens":
            print("Jogador escolheu itens")
            # fazer logica de itens
        elif self.opcoes[self.opcaoSelecionada] == "Fugir":
            print("Jogador escolheu fugir")
            self.mundo.retornar_ao_mundo()

    ############ ATUALIZAÇÃO DO COMBATE ############
    def update(self):
        if not self.combate_ativo:
            return

        self.verificarEstadoCombate()

        if not self.combate_ativo:
            if self.resultado == "vitoria":
                print("Você venceu o combate!")
                self.mundo.retornar_ao_mundo()
                self.jogador.xp = self.jogador.xp + self.inimigo.xp
                return
            elif self.resultado == "derrota":
                print("Você perdeu o combate!")
                self.mundo.retornar_ao_mundo()
                return
############ VERIFICA SE O JOGADOR VENCEU ############
        if self.turno == 0:
            if pyxel.btnp(pyxel.KEY_SPACE):
                print("turno do jogador")
                self.turno = 1
                self.rodada += 1

        elif self.turno == 1:
            print("turno do seu inimigo")
            self.jogador.vida = self.jogador.vida - self.inimigo.dano  
            #fazer o aleatorizador de turnos do inimigo para ele nao ficar atacando sem parar
            self.turno = 0

        if pyxel.btnp(pyxel.KEY_A):
            self.opcaoSelecionada = (self.opcaoSelecionada - 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_D):
            self.opcaoSelecionada = (self.opcaoSelecionada + 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.acoes()

############ DESENHO DO COMBATE INICIADO ############
    def draw(self):
############ ANIMACAO DO COMBATE INICIANDO ############
        if time.time() - self.tempoInicio < 3:
            pyxel.rect(0 + self.xCameraOffset, 0 + self.yCameraOffset, 160, 36, 0)
            pyxel.rect(0 + self.xCameraOffset, 120 + self.yCameraOffset, 160, 36, 0)
            pyxel.text(10 + self.xCameraOffset, 10 + self.yCameraOffset, self.TextosDeAtaque, 7)
############ MENU DE COMBATE ############
        else:
            pyxel.cls(1)
            pyxel.blt(0 + self.xCameraOffset, -64 + self.yCameraOffset, 1, 0, 0, 192, 192)
            pyxel.rect(0 + self.xCameraOffset, 0 + self.yCameraOffset, 160, 36, 0)
            pyxel.blt(50 + self.xCameraOffset, 30 + self.yCameraOffset, 1, 0, 0, 64, 64, 0)  # sprite do inimigo
            pyxel.rect(0 + self.xCameraOffset, 120 + self.yCameraOffset, 160, 36, 0)
            pyxel.text(10 + self.xCameraOffset, 5 + self.yCameraOffset, f"Rodada: {self.rodada}", 7)
            
############ OPCOES DE COMBATE ############
            for i, opcao in enumerate(self.opcoes):
                cor = 7 if i == self.opcaoSelecionada else 6
                pyxel.text(10 + i * 40 + self.xCameraOffset, 120 + self.yCameraOffset, opcao, cor)
############ desenha a barra de vida do jogador ###########
            pyxel.rect(20 + self.xCameraOffset, 106 + self.yCameraOffset, self.jogador.vida, 5, 11)
            pyxel.text(10 + self.xCameraOffset, 106 + self.yCameraOffset, "{}".format(self.jogador.vida), 11)
            
############ desenha a barra de vida do inimigo ############
            pyxel.rect(80 + self.xCameraOffset, 22 + self.yCameraOffset, self.inimigo.vida, 5, 8)

        if self.resultado == 'vitoria':
            pyxel.text(100 + self.xCameraOffset, 5 + self.yCameraOffset, "Voce venceu", 8)
            self.mundo.retornar_ao_mundo()