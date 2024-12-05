import pyxel

class combate:

    def __init__(self):
        self.opcoes = ["Atacar", "Defender", "Itens", "Fugir"]
        self.opcao_selecionada = 0
        self.ativo = True
        self.mensagem = ""
        self.tempo_mensagem = 0
        self.fundo = "D:/Documents_SATA/Faculdade/Python/Jogo/assets/images/Fundo_combate.png"  # Adicione o caminho correto para a imagem de fundo
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
# para fazer as mensagens sumirem
        if self.tempo_mensagem > 0:
            self.tempo_mensagem -= 1
            if self.tempo_mensagem == 0:
                self.mensagem = ""

    def draw(self):
        pyxel.cls(1)
        for i, opcao in enumerate(self.opcoes):
            cor = 10 if i == self.opcao_selecionada else 9
            pyxel.text(10, 70 + i * 10, opcao, cor)
        if self.mensagem:
            pyxel.text(15, 20, self.mensagem, 10)

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
        self.mensagem = "Voce atacou! mas errou :("
        self.tempo_mensagem = 30

    def defender(self):
        # Implementar lógica de defesa
        self.mensagem = "Bloqueio! voce levou um dano ai"
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
