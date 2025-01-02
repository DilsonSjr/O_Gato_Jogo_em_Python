import pyxel
import time

class NPC:
    def __init__(self, x, y, texto, sprite_x, sprite_y, largura, altura, num_quadros=2, intervalo_animacao=0.3):
        self.x = x
        self.y = y
        self.texto = texto
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.largura = largura
        self.altura = altura
        self.num_quadros = num_quadros  # Número de quadros na animação
        self.intervalo_animacao = intervalo_animacao  # Tempo entre quadros
        self.quadro_atual = 0  # Quadro atual da animação
        self.ultimo_tempo = time.time()  # Tempo da última troca de quadro

        self.dialogo = False
        self.tempo_inicio_dialogo = 0

    def detectar_jogador(self, jogador):
        # Verifica se o jogador está próximo ao NPC
        distancia_x = abs(self.x - jogador.x)
        distancia_y = abs(self.y - jogador.y)
        distancia_maxima = 16  # Distância máxima para interação

        if distancia_x <= distancia_maxima and distancia_y <= distancia_maxima:
            # Verifica se a tecla E está sendo apertada
            if jogador.estado == "interagir":
                self.dialogo = True
                self.tempo_inicio_dialogo = time.time()

    def atualizar_animacao(self):
        tempo_atual = time.time()
        if tempo_atual - self.ultimo_tempo >= self.intervalo_animacao:
            self.quadro_atual = (self.quadro_atual + 1) % self.num_quadros
            self.ultimo_tempo = tempo_atual

    def desenhar(self):
        # Atualiza a animação
        self.atualizar_animacao()

        # Calcula a posição do sprite com base no quadro atual
        quadro_offset = self.quadro_atual * self.largura
        pyxel.blt(self.x, self.y, 0, self.sprite_x + quadro_offset, self.sprite_y, self.largura, self.altura, 0)

        # Mostra o diálogo, se ativo
        if self.dialogo:
            linhas = self.texto.split("\n")
            largura_texto = max(len(linha) for linha in linhas) * 4 + 4  # Cada caractere tem 4px de largura
            altura_texto = len(linhas) * 7 + 4  # Cada linha tem 7px de altura
            
            # Calcula posição do fundo do texto para centralizar acima da cabeça do NPC
            pos_fundo_x = self.x + self.largura // 2 - largura_texto // 2
            pos_fundo_y = self.y - altura_texto - 4

            # Desenha o fundo do texto
            pyxel.rect(pos_fundo_x, pos_fundo_y, largura_texto, altura_texto, 0)
            
            # Desenha cada linha de texto centralizada
            for i, linha in enumerate(linhas):
                texto_x = pos_fundo_x + 2
                texto_y = pos_fundo_y + 2 + i * 7
                pyxel.text(texto_x, texto_y, linha, 7)

            # Desativa o diálogo após 3 segundos
            if time.time() - self.tempo_inicio_dialogo >= 3:
                self.dialogo = False