import pyxel
import time
from mundo import Mapa
from jogador import Personagem

class Menu:
    def __init__(self, xCameraOffset, yCameraOffset):
        pyxel.load('../assets/images/bartolomeu.pyxres')
        self.opcoes = ["Jogar", "Creditos", "Fechar"]
        self.opcao_selecionada = 0
        pyxel.playm(1, 1, True) # toca a musica de fundo, 00 é o numero da soundtrack, 1 é os ticks 1 =160, True é se loopa
        self.creditos_start_time = None
        self.mostrando_creditos = False

        self.mostrando_intro = False
        self.intro_start_time = None
        self.intro_duracao = 1 #define o tempo de duraçao da intro, dexa em 1 pra testar e antes de lançar aumenta pra 60

        self.xCameraOffset = xCameraOffset 
        self.yCameraOffset = yCameraOffset

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.mostrando_creditos:
            # Sai dos créditos após 5 segundos ou ao pressionar SPACE
            if pyxel.btnp(pyxel.KEY_SPACE) or (time.time() - self.creditos_start_time > 5):
                self.mostrando_creditos = False
            return

        if self.mostrando_intro:
            # Sai da introdução após o tempo definido
            if time.time() - self.intro_start_time > self.intro_duracao:
                self.mostrando_intro = False
                self.iniciar_jogo()
            return

        # Navegação no menu
        if pyxel.btnp(pyxel.KEY_W):
            self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_S):
            self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.executar_acao()

    def draw(self):
        if self.mostrando_creditos:
            self.draw_creditos()
        elif self.mostrando_intro:
            self.draw_intro()
        else:
            self.draw_menu()

    def draw_menu(self):
        pyxel.cls(1)
        pyxel.blt(0 + self.xCameraOffset, -64 + self.yCameraOffset, 1, 0, 0, 192, 192)
        pyxel.rect(0 + self.xCameraOffset, 100 + self.yCameraOffset, 160, 56, 0)
        for i, opcao in enumerate(self.opcoes):
            cor = 10 if i == self.opcao_selecionada else 9
            pyxel.text(self.xCameraOffset + 10, self.yCameraOffset + 105 + i * 10, opcao, cor)
        pyxel.blt(80 + self.xCameraOffset, 80 + self.yCameraOffset, 1, 0, 176, 64, 64, 2)

    def draw_creditos(self):
        pyxel.cls(0)
        pyxel.text(10, 50, "Trabalho de: \n\nDilson Simões, 166609 \nGuilherme Burkert, xxxxxxx", pyxel.COLOR_WHITE)
        pyxel.text(10,120,"Espere ou \nPressione ESPACO para voltar", pyxel.COLOR_WHITE)

    def draw_intro(self):
        pyxel.cls(0)
        mensagens = [
            "Ola!",
            "bom, essa e a historia\nde como um gato",
            "se tornou rei dos piratas\n  pera nao isso nao ta certo",
            "mestre pokemon\n  nao tambem nao,\n\nbankai? \n  pera ainda nao",
            "JA SEI A CRIACAO DIVINA\nMAIS PODEROSSA\nE AMADA POR TODOS",
            "mas vamos do inicio",
            "eu estava em casa,\nquando bateu uma fominha",
            "e eu fui na cozinha",
            "e encontrei um rato.",
            "o rato olhou para mim e disse:",
            "'aha lero lero oce nao mi pega,\nbleeeh'",
            "Eu, claro, nao resisti\ne fui atrás do rato.",
            "Mas o rato era mais\nrapido do que eu pensava.",
            "eu segui ele pra fora de casa,\npo vista bonitona,",
            "so que um cachorro\nenorme\ntava la ne \n\nobvio",
            "O cachorro me viu e\ncomeçou a correr atras de mim.",
            "ele grito\n'hoje tem file mingnon no jantar'",
            "que dog estupido file mignon\ne carne de boi nao gato",
            "e entao acabei trupicando\ne caindo.",
            "O cachorro me\nalcançou e, bem...",
            "eu acordei dentro dessa casa\n que voce vai ver agora, \nnessa cidade irada",
            "papai ganhou na loteria baby",
        ]
        tempo_por_mensagem = self.intro_duracao / len(mensagens)
        indice = int((time.time() - self.intro_start_time) / tempo_por_mensagem)
        if indice < len(mensagens):
            pyxel.text(20, 50, mensagens[indice], pyxel.COLOR_WHITE)

    def executar_acao(self):
        if self.opcao_selecionada == 0:
            self.mostrar_intro()
        elif self.opcao_selecionada == 1:
            self.mostrar_creditos()
        elif self.opcao_selecionada == 2:
            self.fechar()

    def mostrar_intro(self):
        self.intro_start_time = time.time()
        self.mostrando_intro = True

    def mostrar_creditos(self):
        self.creditos_start_time = time.time()
        self.mostrando_creditos = True

    def iniciar_jogo(self):
        Mapa(Personagem(130, 420)) 

    def fechar(self):
        pyxel.close()
