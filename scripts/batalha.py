import pyxel
import random
import time

class Combate():

############ INICIALIZAÇÃO DO COMBATE ############
    def __init__(self, Jogador, Inimigo):
        self.jogador = Jogador
        self.inimigo = Inimigo
        self.turno = 0  # 0 para jogador, 1 para inimigo
        self.rodada = 0
        self.opcoes = ["Atacar", "Especial","itens","Fugir"]
        self.opcaoSelecionada = 0
        self.selecionarOpcao = 0

        self.xCameraOffset = self.jogador.xCameraOffset
        self.yCameraOffset = self.jogador.yCameraOffset


############ ATRIBUTOS DO COMBATE ############
        self.jogador.vida = self.jogador.vida
        self.jogador.dano = self.jogador.dano
        self.inimigo.vida = self.inimigo.vida

############ DEBUG DO COMBATE ############
        print("dano ",self.jogador.dano)
        print("vida ",self.jogador.vida)
        print("inimigo dano ",self.inimigo.dano)
        print("inimigo vida ",self.inimigo.vida)    

############ TEXTOS DO COMBATE ############
        self.TextosDeAtaque = random.choice([
    "Prepare-se para sentir minhas \ngarras,invasor!",
    "Voce ousa entrar no meu \nterritorio?Vai pagar por isso!",
    "Hora de mostrar quem e o \nverdadeiro rei deste quintal!",
    "Minhas patas nao falham! \nVenha se atrever!",
    "Voce acabou de arranjar uma \nbriga que nao pode vencer, miado fraco!",
    "Eu estava so cochilando,\nmas agora vou te ensinar uma licao!",
    "Prepare-se para um \nverdadeiro duelo felino!",
    "Suas chances sao tao boas quanto \num ratono meio de uma colonia de gatos!",
    "Voce e corajoso, mas nao sera\n pario para minhas presas afiadas!",
    "Miau, miau... Hora de lutar\nate o ultimo pelo!"])
        self.tempoInicio = time.time()
        pyxel.run(self.update, self.draw)

############# AÇÕES DO COMBATE ############ mover para o jogador.py depois
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
            # faazer logica de itens
        elif self.opcoes[self.opcaoSelecionada] == "Fugir":
            print("Jogador escolheu fugir")
            # fazer lógica de fugir

############ ATUALIZAÇÃO DO COMBATE ############
    def update(self):
        
        self.resultado = 0

        if self.inimigo.vida <= 0:
            self.resultado = 1
        elif self.jogador.vida <= 0:
            self.resultado = 2

        if self.turno == 0:
                if pyxel.btnp(pyxel.KEY_SPACE):
                    print("turno do jogador")
                    self.turno = 1
                    self.rodada += 1
        
        elif self.turno == 1:
                print("turno do seu inimigo")
                self.jogador.vida = self.jogador.vida - self.inimigo.dano # fazer o aleatorizador de turnos do inimigo para ele nao ficar atacando sem parar
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
            pyxel.rect(0 + self.xCameraOffset,0 + self.yCameraOffset, 160, 36, 0)
            pyxel.rect(0 + self.xCameraOffset, 120 + self.yCameraOffset, 160, 36, 0)
            pyxel.text(10 + self.xCameraOffset, 10 + self.yCameraOffset, self.TextosDeAtaque, 7)
            

############ MENU DE COMBATE ############
        else:
            pyxel.cls(1)
            pyxel.blt(0 + self.xCameraOffset,- 64 + self.yCameraOffset, 1,0,0,192,192,)
            pyxel.rect(0 + self.xCameraOffset,0 + self.yCameraOffset, 160, 36, 0)
            pyxel.blt(50 + self.xCameraOffset, 30 + self.yCameraOffset, 1,0,0,64,64,0) # sprite do inimigo
            pyxel.rect(0 + self.xCameraOffset, 120 + self.yCameraOffset, 160, 36, 0)
            pyxel.text(10 + self.xCameraOffset, 5 + self.yCameraOffset, f"Rodada: {self.rodada}", 7) 
            # OPCOES
            for i, opcao in enumerate(self.opcoes):
                cor = 7 if i == self.opcaoSelecionada else 6
                pyxel.text(10 + i * 40 + self.xCameraOffset, 120 + self.yCameraOffset, opcao, cor)
############ desenha a barra de vida do jogador ###########
            pyxel.rect(20 + self.xCameraOffset, 106 + self.yCameraOffset, self.jogador.vida, 5 , 11) 
            pyxel.text(10 + self.xCameraOffset, 106 + self.yCameraOffset, "{}".format(self.jogador.vida), 11)

############ desenha a barra de vida do inimigo ############
            pyxel.rect(80 + self.xCameraOffset, 22 + self.yCameraOffset, self.inimigo.vida, 5 , 8)
        
        if self.resultado == 1:
            pyxel.text(130 + self.xCameraOffset, 5 + self.yCameraOffset, "Voce venceu", 8)
            ### programar pra sair do combate 

        elif self.resultado == 2:
            pyxel.cls(0)
            pyxel.text(self.xCameraOffset, 50 + self.yCameraOffset, "Voce perdeu", 8)