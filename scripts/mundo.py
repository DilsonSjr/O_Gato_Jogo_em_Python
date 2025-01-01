import pyxel
import time
from jogador import Personagem
from inimigo import Inimigo
from NPC import NPC
from batalha import Combate

class Porta:
    def __init__(self, x1, y1, x2, y2, largura=16, altura=16, cooldown=1):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.largura, self.altura = largura, altura
        self.cooldown = cooldown
        self.ultimo_uso = -cooldown  # pra ele nao poder entrar direto

    def verificar_porta(self, jogador):
        tempo_atual = time.time()

        if tempo_atual - self.ultimo_uso < self.cooldown:# Verifica se o cooldown já passou
            return

        # Verifica se o jogador está na área da primeira porta pra nao ter que ser um pixel especifico
        if self.x1 <= jogador.x < self.x1 + self.largura and self.y1 <= jogador.y < self.y1 + self.altura:
            jogador.x, jogador.y = self.x2, self.y2
            self.ultimo_uso = tempo_atual  # Atualiza o tempo do último uso
            print(f"Entrou na porta de ({self.x1}, {self.y1}) para ({self.x2}, {self.y2})")

        elif self.x2 <= jogador.x < self.x2 + self.largura and self.y2 <= jogador.y < self.y2 + self.altura:
            jogador.x, jogador.y = self.x1, self.y1
            self.ultimo_uso = tempo_atual  # Atualiza o tempo do último uso
            print(f"Entrou na porta de ({self.x2}, {self.y2}) para ({self.x1}, {self.y1})")

class Mapa:
    def __init__(self, jogador):
        pyxel.load('../assets/images/bartolomeu.pyxres')   
        pyxel.playm(0, 1, True)  # Toca a música de fundo
        self.jogador = jogador
        self.inimigo = Inimigo(200, 420)
        self.npc = NPC(268, 377, self.jogador)

############ Posições das portas        
        self.portas = [
            Porta(1036, 207, 130, 450), # casa do player
            Porta(1081, 558, 310, 367), # GIM (ginasio)
            Porta(452,352,1337,239), # Miaws (mercadinho)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.mover()
        self.npc.detectar_jogador()

        # Verifica passagem para cada porta
        for porta in self.portas:
            porta.verificar_porta(self.jogador)

        # Log para debug das posições
        print(f"Posição do jogador: ({self.jogador.x}, {self.jogador.y})")

        # Verifica se as posições do jogador e do inimigo coincidem
        if (self.jogador.x == self.inimigo.x and self.jogador.y in range(self.inimigo.y - 50, self.inimigo.y + 50)) or \
            (self.jogador.y == self.inimigo.y and self.jogador.x in range(self.inimigo.x - 50, self.inimigo.x + 50)):
            Combate(self.jogador, self.inimigo, self)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 2000, 2000)  # Ajuste as dimensões do mapa conforme necessário
        self.inimigo.desenhar()
        self.jogador.desenhar()
        self.npc.desenhar()

    def retornar_ao_mundo(self):
        pyxel.run(self.update, self.draw)
