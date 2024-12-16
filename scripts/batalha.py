import pyxel
import random
import time

from jogador import Personagem
from inimigo import inimigo
class combate:

############ INICIALIZAÇÃO DO COMBATE ############
    def __init__(self):
        self.jogador = Personagem(0,0)
        self.inimigo = inimigo(0,0, self.jogador)
        self.turno = 0  # 0 para jogador, 1 para inimigo
        self.rodada = 0
        self.opcoes = ["Atacar", "Especial","itens","Fugir"]
        self.opcaoSelecionada = 0
        self.selecionarOpcao = 0


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
    "Prepare-se para sentir minhas garras,\ninvasor!",
    "Voce ousa entrar no meu territorio?\nVai pagar por isso!",
    "Hora de mostrar quem e o verdadeiro\nrei deste quintal!",
    "Minhas patas nao falham!\nVenha se atrever!",
    "Voce acabou de arranjar uma briga\nque nao pode vencer, miado fraco!",
    "Eu estava so cochilando, mas agora\nvou te ensinar uma licao!",
    "Prepare-se para um verdadeiro\nduelo felino!",
    "Suas chances sao tao boas quanto um rato\nno meio de uma colonia de gatos!",
    "Voce e corajoso, mas nao sera pario\npara minhas presas afiadas!",
    "Miau, miau... Hora de lutar ate\no ultimo pelo!"])
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
            pyxel.rect(0,0, 192, 27, 0)
            pyxel.rect(0, 88, 192, 27, 0)
            pyxel.text(10, 10,self.TextosDeAtaque, 7)
            

############ MENU DE COMBATE ############
        else:
            pyxel.cls(1)
            pyxel.blt(0,-64,1,0,0,192,192,)
            pyxel.rect(0,0, 192, 14, 0)
            pyxel.blt(60,30,1,0,0,64,64,0) # sprite do inimigo
            pyxel.rect(0, 88, 192, 27, 0)
            pyxel.text(10, 5, f"Rodada: {self.rodada}", 7) 
            # OPCOES
            for i, opcao in enumerate(self.opcoes):
                cor = 7 if i == self.opcaoSelecionada else 6
                pyxel.text(10 + i * 50, 95, opcao, cor)
############ desenha a barra de vida do jogador ############


            pyxel.rect(20, 86, self.jogador.vida, 5 , 11) 
            pyxel.text(10, 86, "{}".format(self.jogador.vida), 11)

############ desenha a barra dde vida do inimigo ############
            pyxel.rect(80, 22, self.inimigo.vida, 5 , 8)
        
        if self.resultado == 1:
            pyxel.text(130, 5, "Voce venceu", 8)
            ### programar pra sair do combate 
        elif self.resultado == 2:
            pyxel.cls(0)
            pyxel.text(50, 50, "Voce perdeu", 8)
