import pyxel

class Personagem:

    def __init__(self, x, y):
        d6 = pyxel.rndi(1, 6)
        self.time =  0

        self.x = x 
        self.y = y 
        self.velocidade = 1

        self.vida = d6 + 12
        self.dano = d6 + 30
        self.xp = 0
        self.estado = 'parado'  
        self.direcao = 'direita'  
        self.xTamanhoSprite = 16
        self.yTamanhoSprite = 16

        self.frame = 0
        self.contadorAnimacao = 50 

        self.xCameraOffset = self.x - pyxel.width // 2 + 10
        self.yCameraOffset = self.y - pyxel.height // 2 + 10

    def atualizar_d6(self):

        # Define um valor aleatorio para o dano
        d6 = pyxel.rndi(3, 5)
        self.dano = d6

    def verificarColisao(self, novo_x, novo_y):
        tamanhoTile =8   # Tamanho do tile em pixels
        
        # Converte a posição do jogador para o sistema de coordenadas do tile
        tile_x = int(novo_x // tamanhoTile +1.5) # Valores para corrigir a hitbox
        tile_y = int(novo_y // tamanhoTile +2) # valores para corrigir a hitbox
        
        # Obtém a cor do tile na nova posição
        corTile = pyxel.tilemaps[1].pget(tile_x, tile_y)[1]
        
        # Verifica se a cor do tile é diferente de 0 (o que significa que há um obstáculo)
        if corTile == 0:
            
            return False  # Colisão detectada
        return True  # Não há colisão, o gato pode andar

    def controle (self, tecla, eixo, velocidade, direcao, tamanhoSprite):
        
        # Verifica se a tecla foi pressionada
        if pyxel.btn(tecla):  
            # 'Prediz' a nova posição do jogador
            nova_posicao = getattr(self, eixo) + velocidade

            # Atualiza a posicao com base no eixo
            if eixo == 'y':
                # Verifica se a nova posição não colide com o mapa
                if not self.verificarColisao(self.x, nova_posicao):
                    self.direcao = f'{direcao}'
                    self.estado = 'andando'
                    self.y = nova_posicao
                    
            elif eixo == 'x':
                # Verifica se a nova posição não colide com o mapa
                if not self.verificarColisao(nova_posicao, self.y):
                    self.direcao = f'{direcao}'
                    self.estado = 'andando'
                    self.xTamanhoSprite =  (tamanhoSprite) * abs(self.xTamanhoSprite)
                    self.x = nova_posicao

    def mover(self):

        # Botoes de jogo
        self.controle(pyxel.KEY_A, 'x', -self.velocidade, 'esquerda', -1)
        self.controle(pyxel.KEY_D, 'x', self.velocidade, 'direita', 1)
        self.controle(pyxel.KEY_W, 'y', -self.velocidade, 'cima', 0)
        self.controle(pyxel.KEY_S, 'y', self.velocidade, 'baixo', 0)
        
        # Verifica interacao
        if pyxel.btn(pyxel.KEY_E):
            self.estado = 'interagir'

        if self.xp >= 10: 
            self.vida += 5
            self.dano += 2
            self.xp -= 10

        # # Habilita sprint #desabilitado por conta do ritmo do jogo
        # if pyxel.btn(pyxel.KEY_SHIFT):
        #     self.velocidade = 1.5
        # else:
        #     self.velocidade = 1

        # Detecta quando as teclas de movimento sao liberadas
        if pyxel.btnr(pyxel.KEY_A) or pyxel.btnr(pyxel.KEY_D) or pyxel.btnr(pyxel.KEY_W) or pyxel.btnr(pyxel.KEY_S):
            self.estado = 'parado'

    def animacoes(self):
        
        if self.estado == "parado":
            self.contadorAnimacao += 1

            if self.contadorAnimacao >= 10:
                self.frame += 16
                self.contadorAnimacao = 0

            if self.frame > 48:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 0, self.xTamanhoSprite, self.yTamanhoSprite, 0)

        if self.estado == 'andando':
            self.contadorAnimacao += 1

            if self.contadorAnimacao >= 10:
                self.frame += 16
                self.contadorAnimacao = 0

            if self.frame > 96:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 64, self.xTamanhoSprite, self.yTamanhoSprite, 0)

        if self.estado == 'interagir':
            self.contadorAnimacao += 1 

            if self.contadorAnimacao >= 10:
                self.frame += 16 
                self.contadorAnimacao = 0 

            if self.frame > 96-16:
                self.frame = 0

            pyxel.blt(self.x, self.y, 0, self.frame, 112, self.xTamanhoSprite, self.yTamanhoSprite, 0)
            if self.frame == 96-16:
                self.estado = "parado"

    def desenhar(self):

        # Atualiza o offset da camera
        self.xCameraOffset = self.x - pyxel.width // 2 + 10
        self.yCameraOffset = self.y - pyxel.height // 2 + 10

        # Atualiza a camera
        pyxel.camera(self.xCameraOffset, self.yCameraOffset )

        # Desenha a barra de vida
        pyxel.rect(self.xCameraOffset + 20, self.yCameraOffset + 9, self.vida, 5, 0)  
        pyxel.rect(self.xCameraOffset + 19, self.yCameraOffset + 10, self.vida, 5, 8) 
        
        pyxel.text(self.xCameraOffset + 11, self.yCameraOffset + 9, "{}".format(self.vida), 0)
        pyxel.text(self.xCameraOffset + 10, self.yCameraOffset + 10, "{}".format(self.vida), 8)

        # Desenha a barra de xp
        pyxel.rect(self.xCameraOffset + 16, self.yCameraOffset + 19, self.xp, 5, 0)  
        pyxel.rect(self.xCameraOffset + 15, self.yCameraOffset + 20, self.xp, 5, 6) 

        pyxel.text(self.xCameraOffset + 11, self.yCameraOffset + 19, "{}".format(self.xp), 0)
        pyxel.text(self.xCameraOffset + 10, self.yCameraOffset + 20, "{}".format(self.xp), 6)

        # Atualiza e desenha as animacoes
        self.animacoes()