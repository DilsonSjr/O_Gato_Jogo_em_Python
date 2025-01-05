import pyxel
import time
from inimigo import Inimigo
from NPC import NPC
from batalha import Combate
from finais import Final

class Porta:
    def __init__(self, x1, y1, x2, y2, largura=16, altura=16, cooldown=1):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.largura, self.altura = largura, altura
        self.cooldown = cooldown
        self.ultimo_uso = -cooldown  # pra ele nao poder entrar direto na porta

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
        pyxel.load('../assets/bartolomeu.pyxres')
        self.boss_fight =  True   
        pyxel.playm(0, 1, True)  # Toca a música de fundo

############ Posições das portas        
        self.portas = [
            Porta(1036, 207, 130, 450), # casa do player
            Porta(1081, 558, 310, 367), # GIM (ginasio)

            Porta(1058,456, 1303,558), # porta errada1 gim inicio #####
            Porta(1081,456, 1303,813), # porta errada2 gim inicio #####
            Porta(1105,456, 1017, 750),# porta CERTA3 gim inicio #####

            Porta(991,690, 1015, 1005),# porta CERTA1 gim 2 sala ####
            Porta(1016,690, 1495,558),# porta errada2 gim 2 sala #### 
            Porta(1040,690, 1495, 813),# porta errada3 gim 2 sala ####

            Porta(994,943, 1686,558),# porta errada1 gim 3 sala
            Porta(1017,943,1686,813),# porta errada2 gim 3 sala
            Porta(1041,943,1271,1070),# porta certa gim 3 sala -> boss

        
            Porta(452,352,1337,239), # Miaws (mercadinho)

        ]

############ desenha os NPCS
        self.npcs = [
            NPC(268,377, "Iae cara, voce e novo aqui nao e ?", 0, 176, 16, 16, num_quadros=4, intervalo_animacao=0.2),
            NPC(280,400, "Cara eu ate queria sair da Gatopolis,\nmas o tutui guarda a chave do portão", 16, 192, 16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(296,400, "tutui é o gato mais forte daqui,\nvive na academia", 48, 208, -16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(440,398, "ai que delicia esse picole", 64, 176, 16, 16, num_quadros=3, intervalo_animacao=0.2),
            NPC(294,246, "Uma caixinha de papelao\nera meu sonho agora", 0, 240, 16, 16, num_quadros=3, intervalo_animacao=0.1),
            NPC(600,200, "Cerebros,\n cerebros fresquinhos,\neu quero cerebros fresquinhossss", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(244,500, "eu juro proce, Gatopolis instiga\ntodo mundo a falar errado", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(211,530, "eu to ocupado tentando nao falar com voce ok?\nsai fora", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(210,577, "EQUIPAR UM ITEM FAZ VOCE FICAR MAIS FORTE\ndesculpa eu sempre quis ser tutorial \nde um jogo em vida", 0, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(215,587, "qui saudadi de passa o dia todo fazendo nada so\n ZzZ", 64, 208, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(278,610, "virei policial aqui so pelo distintivo brilhante", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(436,704, "queria entra pra academia,\nmas o tutui so deixa os de verdade la", 64, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(578,756, "queria comprar um terninho\nmas eu sou tao pobrin", 0, 208, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(534,844, "nao fala comigo nao que\neu to trevoso", 0, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(475,844, "nao, olhe, para a luz vermelha", 0, 160, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(368,878, "nao tem um inseto pra cacar\nque odio", 0, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(268,774, "novelo di la\num item di luxo por essas bandas\nsim", 128, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(376,384, "hey toma cuidado,\nexistem gatos perigosos por aqui", 112, 224, -16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(132,212, "ai eu adoro praia, mas essa areia te conta", 64, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(548,134, "essa cidade e muito BRAT meo", 64, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(613,126, "aquele portao dourado, e a saida de gatopolis,\ndizem que tudo e possivel apartir dele ", 0, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(687,283, "ei amor olha aquele peixe la", 0, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(687,300, "se eu tivesse uma vara de pesca\nele ja tava fritin", 64, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(415,423, "Verdade que picole bom, é de frango?", 64, 192, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(589,501, "queria ir no show da Miewllie catish\nvoce conhece? ela canta\n\nmeaw, meaw, meaw", 64, 176, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(627,547, "ei me conta como vc veio parar aqui?", 128, 240, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1307,190, "bem vindo ao miaws\n como posso ajudar?", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1307,209, "cara a gente ja bateu a meta\nnao vamo vende nada hoje nao", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1219,1028, "O tutui vai quebra tua cara", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1219,998, "aqui nao tem lance pra tu bigode fraco", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1219,998, "RA aporrstei\nCinquentrrao no tutuirr", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1090,526, "Bem vindo ao GIM,\ntenha certeza de que voce deve estar aqui", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1068,526, "Voce tem que ser forte\npra sair daqui com vida", 128, 224, 16, 16, num_quadros=3, intervalo_animacao=0.3),
            NPC(1272,989, "EU SOU O TUTUI O LARGATAO\nE EU MANDO NESSE LUGAR", 128, 192, 16, 16, num_quadros=3, intervalo_animacao=0.1),
            ]

        self.inimigo = [Inimigo(213, 423, 8, 3, 128, 208, "Minhas patas nao falham!\nVenha se atrever!"),
                        Inimigo(318, 544, 10, 3, 128, 208, "Hora de mostrar quem e o verdadeiro\nrei deste quintal!"),
                        Inimigo(506, 255, 10, 3, 128, 208, "Eu estava so cochilando, mas agora\nvou te ensinar uma licao!"),
                        Inimigo(460, 510, 10, 3, 128, 208, "Voce e corajoso, mas nao sera pario\npara minhas presas afiadas!"),
                        Inimigo(612, 956, 12, 4, 128, 208, "Prepare-se para um verdadeiro\nduelo felino!"),
                        Inimigo(279, 842, 14, 6, 128, 208, "Voce ousa entrar no meu territorio?\nVai pagar por isso!"),
                        Inimigo(1687, 768, 14, 6, 128, 208, "Voce nao passara por mim!\nPrepare-se para a batalha!"),
                        Inimigo(1689, 507, 14, 6, 128, 208, "voce estragou meu treino\nbigode fraco"),
                        Inimigo(1303, 512, 15, 6, 128, 208, "sera que voce é capaz?"),
                        Inimigo(1305, 767, 15, 6, 128, 208, "Tenho que correr, tenho que..."),
                        Inimigo(1496, 507, 14, 6, 128, 208, "Ain Tutui malvadao"),
                        Inimigo(1496, 767, 14, 6, 128, 208, "voce vai morrer! Denovo!"),
                        ]

        self.jogador = jogador

        pyxel.run(self.update, self.draw)

    def update(self):

    # Atualiza cada NPC
        for npc in self.npcs:
            npc.detectar_jogador(self.jogador)

        self.jogador.mover()

        # Verifica passagem para cada porta
        for porta in self.portas:
            porta.verificar_porta(self.jogador)

        # Log pra debug das posições (usando pra saber as posiçoes das portas)
        print(f"Posição do jogador: ({self.jogador.x}, {self.jogador.y})")
        
        for inimigo in self.inimigo:
            if inimigo.vida > 0 and not inimigo.time > 0:
                if (self.jogador.x == inimigo.x and self.jogador.y in range(inimigo.y - 40, inimigo.y + 40)) or \
                    (self.jogador.y == inimigo.y and self.jogador.x in range(inimigo.x - 40, inimigo.x + 40)):
                    Combate(self.jogador, inimigo, self)

        todos_sem_vida  = all(inimigo.vida <= 0 for inimigo in self.inimigo)

        if todos_sem_vida and self.boss_fight:
            self.npcs.pop()
            self.inimigo.append(Inimigo(1272,989, 30, 6, 128, 192, "Voce acabou de arranjar uma briga\nque nao pode vencer, miado fraco!"))
            self.boss_fight = False
        elif todos_sem_vida and not self.boss_fight and self.jogador.x in range(376 - 20, 376 + 20) and self.jogador.y in range(80, 80 + 20):
            Final("ganhou", self.jogador)
        elif self.jogador.vida <= 0:
            Final("morreu", self.jogador)
            

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 2000, 2000) #mapa tem que ser enorme pra caber as casas do lado de fora do mapa
        self.jogador.desenhar()

# Desenha cada NPC
        for npc in self.npcs:
            npc.desenhar()

        for inimigo in self.inimigo:
            inimigo.desenhar()

    def retornar_ao_mundo(self):
        pyxel.run(self.update, self.draw)
