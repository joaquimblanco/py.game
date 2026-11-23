import os
import pygame
pygame.init()
LARGURA = 960
ALTURA = 560
TAM = 40
GRAVIDADE = 0.5
FORCA_PULO = 10
VELOCIDADE = 3
LARANJA = (232, 151, 66)
PRETO = (22, 21, 29)
CINZA = (45, 43, 56)
VERMELHO = (226, 59, 75)
VERDE = (56, 192, 122)
VERDE_ESCURO = (14, 61, 39)
BRANCO = (255, 255, 255)
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Fase Maldita")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)
fonte_grande = pygame.font.Font(None, 96)
mapa1 = [
    "########################",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#.P.............^....D.#",
    "##########XXX###########",
    "##########^^^###########",
]
mapa2 = [
    "########################",
    "#......................#",
    "#......................#",
    "#......................#",
    "#.......F..............#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#.P.........H.....^..D.#",
    "########################",
    "########################",
]
mapa3 = [
    "########################",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#.P................D.E.#",
    "#######..I..I..I.#######",
    "#######^^^^^^^^^^#######",
]
mapa4 = [
    "########################",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#.P...C..^...^...T..D.d#",
    "########################",
    "########################",
]
mapas = [mapa1, mapa2, mapa3, mapa4]
class quadrado:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y  # faltava esta linha na versão antiga
        self.velocidade_y = 0
        self.no_chao = False  # o loop avisa quando tem bloco embaixo
    def mover(self, deslocamento_x, deslocamento_y):
        self.x += deslocamento_x
        self.y += deslocamento_y
    def pular(self):
        if self.no_chao:  # só pula se estiver em cima de um bloco
            self.velocidade_y = -FORCA_PULO
def desenhar_bloco(rect):
    pygame.draw.rect(tela, PRETO, rect)
    pygame.draw.rect(tela, CINZA, (rect.x, rect.y, rect.width, 4))
def desenhar_porta(rect):
    moldura = (rect.x - 3, rect.y - 3, rect.width + 6, rect.height + 6)
    pygame.draw.rect(tela, VERDE_ESCURO, moldura)
    pygame.draw.rect(tela, VERDE, rect)
    pygame.draw.circle(tela, VERDE_ESCURO, (rect.right - 5, rect.centery), 2)
def desenhar_espinho(rect):
    pygame.draw.polygon(tela, VERMELHO, [rect.bottomleft, rect.midtop, rect.bottomright])
def escrever(texto, qual_fonte, y, cor):
    imagem = qual_fonte.render(texto, True, cor)
    x = (LARGURA - imagem.get_width()) // 2
    tela.blit(imagem, (x, y))
pasta = os.path.dirname(os.path.abspath(__file__))
tem_som = False
if os.path.exists(pasta + "/sons") and pygame.mixer.get_init():
    tem_som = True
    som_pulo = pygame.mixer.Sound(pasta + "/sons/pulo.wav")
    som_morte = pygame.mixer.Sound(pasta + "/sons/morte.wav")
    som_porta = pygame.mixer.Sound(pasta + "/sons/porta.wav")
    som_pulo.set_volume(0.4)
    som_morte.set_volume(0.5)
    som_porta.set_volume(0.5)
    pygame.mixer.music.load(pasta + "/sons/musica.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
estado = "menu"
comecar_fase = False
rodando = True
while rodando:
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # ESC fecha o jogo
                rodando = False
            if estado == "menu":
                if evento.key == pygame.K_RETURN:
                    fase = 0
                    estado = "jogando"
                    comecar_fase = True
            elif estado == "jogando":
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_w or evento.key == pygame.K_UP:
                    if posicao_quadrado.no_chao and tem_som:
                        som_pulo.play()
                    posicao_quadrado.pular()
    if comecar_fase:
        comecar_fase = False
        blocos = []
        espinhos = []
        mapa = mapas[fase]
        for linha in range(len(mapa)):
            for coluna in range(len(mapa[linha])):
                letra = mapa[linha][coluna]
                x = coluna * TAM
                y = linha * TAM
                if letra == "#" or letra == "X" or letra == "I":  # X e I: bloco normal por enquanto
                    blocos.append(pygame.Rect(x, y, TAM, TAM))
                elif letra == "^":
                    espinhos.append(pygame.Rect(x, y + 20, TAM, 20))
                elif letra == "D":
                    porta = pygame.Rect(x + 8, y, 24, TAM)
                elif letra == "P":
                    posicao_quadrado = quadrado("preto", x, y)  # nasce onde está o P
    if estado == "jogando":
        teclas = pygame.key.get_pressed()
        velocidade_x = 0
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            velocidade_x = VELOCIDADE
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            velocidade_x = -VELOCIDADE
        posicao_quadrado.mover(velocidade_x, 0)  # primeiro anda para os lados
        caixa = pygame.Rect(posicao_quadrado.x, posicao_quadrado.y, TAM, TAM)
        for bloco in blocos:
            if caixa.colliderect(bloco):
                if velocidade_x > 0:
                    posicao_quadrado.x = bloco.left - TAM  # bateu na parede da direita
                if velocidade_x < 0:
                    posicao_quadrado.x = bloco.right  # bateu na parede da esquerda
                caixa.x = posicao_quadrado.x
        posicao_quadrado.velocidade_y += GRAVIDADE  # a gravidade puxa para baixo
        posicao_quadrado.mover(0, int(posicao_quadrado.velocidade_y))  # depois sobe ou desce
        caixa.y = posicao_quadrado.y
        for bloco in blocos:
            if caixa.colliderect(bloco):
                if posicao_quadrado.velocidade_y > 0:
                    posicao_quadrado.y = bloco.top - TAM  # caiu em cima do bloco
                else:
                    posicao_quadrado.y = bloco.bottom  # bateu a cabeça no bloco
                posicao_quadrado.velocidade_y = 0
                caixa.y = posicao_quadrado.y
        pes = caixa.move(0, 1)  # cópia do quadrado 1 pixel abaixo
        posicao_quadrado.no_chao = False
        for bloco in blocos:
            if pes.colliderect(bloco):  # tem bloco embaixo dos pés
                posicao_quadrado.no_chao = True
        for espinho in espinhos:
            if caixa.colliderect(espinho):  # morreu: recomeça a fase
                comecar_fase = True
        if posicao_quadrado.y > ALTURA:  # caiu para fora da tela: recomeça a fase
            comecar_fase = True
        if comecar_fase and tem_som:
            som_morte.play()
        if caixa.colliderect(porta):  # chegou na porta: próxima fase
            if tem_som:
                som_porta.play()
            fase += 1
            if fase < len(mapas):
                comecar_fase = True
            else:
                estado = "menu"  # acabaram as fases: volta para o menu
    if estado == "menu":
        tela.fill(PRETO)
        escrever("FASE MALDITA", fonte_grande, 60, LARANJA)
        escrever("Chegue na porta verde... se ela deixar.", fonte, 160, BRANCO)
        escrever("Aperte ENTER para começar", fonte, 260, LARANJA)
    elif estado == "jogando":
        tela.fill(LARANJA)
        for bloco in blocos:
            desenhar_bloco(bloco)
        for espinho in espinhos:
            desenhar_espinho(espinho)
        desenhar_porta(porta)
        pygame.draw.rect(tela, PRETO, (posicao_quadrado.x, posicao_quadrado.y, TAM, TAM))
    pygame.display.flip()
pygame.quit()