import pyxel
from jogador import Personagem
class combate:

    def __init__(self):
        self.jogador = Personagem(70, 50)
        self.opcoes = ["Atacar", "Defender", "Itens", "Fugir"]
        self.opcao_selecionada = 0
        self.ativo = True
        self.mensagem = ""
        self.tempo_mensagem = 0
        self.fundo = "assets\images\Fundo_combate.png"  
        pyxel.images[0].load(0, 0, self.fundo)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.ativo:
            return
        
        if pyxel.btnp(pyxel.KEY_W):
            self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_S):
            self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.executar_acao()

    def draw(self):
        pyxel.cls(1)
        for i, opcao in enumerate(self.opcoes):
            cor = 10 if i == self.opcao_selecionada else 9
            pyxel.text(10, 70 + i * 10, opcao, cor)
        if self.mensagem:
            pyxel.text(15, 20, self.mensagem, 10)
        pyxel.rect(20, 10, self.jogador.vida,5 , 8) # desenha a barra de vida do
        pyxel.text(10, 10, "{}".format(self.jogador.vida), 8) # desenha em numeros a vida
        # voce morreu
        if self.jogador.vida <= 0:
            pyxel.text(50, 50, "Voce morreu", 8)
    def executar_acao(self):
        if self.opcao_selecionada == 0:
            self.atacar()
        elif self.opcao_selecionada == 1:
            self.defender()
        elif self.opcao_selecionada == 2:
            self.usar_itens()
        elif self.opcao_selecionada == 3:
            self.fugir()

    def atacar(self):
        # Implementar lógica de ataque
        if self.jogador.dano == 6:
            self.mensagem = "Voce atacou! e causou {} de dano NOSSA ISSO FOI CRITICO".format(self.jogador.dano)
        if self.jogador.dano == 1:
            self.mensagem = "Voce atacou! e causou {} de dano, Voce esqueceu de usar as unhas ne".format(self.jogador.dano)
        else:
            self.mensagem = "Voce atacou! e causou {} de dano".format(self.jogador.dano)
        self.tempo_mensagem = 30

    def defender(self):
        # Implementar lógica de defesa
        self.mensagem = "Bloqueio! voce levou {} de dano".format(self.jogador.dano // 2)
        self.tempo_mensagem = 30

    def usar_itens(self):
        # Implementar lógica de uso de itens
        self.mensagem = "Voce nao tem itens"
        self.tempo_mensagem = 60

    def fugir(self):
        # Implementar lógica de fuga
        self.mensagem = "Fugiu"
        self.tempo_mensagem = 30
        self.ativo = False
