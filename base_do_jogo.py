import pygame 
pygame.init() 
tela = pygame.display.set_mode((960, 560)) 
pygame.display.set_caption("Fase malidita")
gravidade = 0.5
chao_y = 500 
tamanho = 40
forca_pulo = 10  
class quadrado: 
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x 
        self.velocidade_y = 0 
    def mover(self, deslocamento_x, deslocamento_y):
        self.x += deslocamento_x 
        self.y += deslocamento_y
    def pular(self):  
        if self.y + tamanho >= chao_y:
            self.velocidade_y = -forca_pulo 
posicao_quadrado = quadrado("preto", 100, 300)
timer = pygame.time.Clock()
rodando = True
while rodando: 
    timer.tick(60) 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if ( evento.key == pygame.K_SPACE or evento.key == pygame.K_w or evento.key == pygame.K_UP):
                posicao_quadrado.pular()
    teclas = pygame.key.get_pressed()
    velocidade_x = 0 
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        velocidade_x = 3
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]: 
        velocidade_x = -3
    posicao_quadrado.velocidade_y += gravidade
    posicao_quadrado.mover(velocidade_x,posicao_quadrado.velocidade_y)
    if posicao_quadrado.y + tamanho >= chao_y: 
        posicao_quadrado.y = chao_y - tamanho
        posicao_quadrado.velocidade_y = 0
    if posicao_quadrado.x > 960:
        posicao_quadrado.x = 0
    tela.fill((232, 151, 66))
    pygame.draw.rect(tela,(80, 130, 50),(0, chao_y, 960, 560 - chao_y))
    pygame.draw.rect(tela, (0, 0, 0),(int(posicao_quadrado.x),int(posicao_quadrado.y),tamanho,tamanho))
    pygame.display.flip()
pygame.quit() 
import pygame 
pygame.init()
LARGURA = 960
ALTURA = 560
TAM = 40 
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
estado = "menu" 
comecar_fase = False  
rodando = True
while rodando: 
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if estado == "menu":
                if evento.key == pygame.K_RETURN:
                    fase = 0
                    estado = "jogando"
                    comecar_fase = True
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
                if letra == "#":
                    blocos.append(pygame.Rect(x, y, TAM, TAM))
                elif letra == "^":
                    espinhos.append(pygame.Rect(x, y + 20, TAM, 20))
                elif letra == "D":
                    porta = pygame.Rect(x + 8, y, 24, TAM)
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
    pygame.display.flip()
pygame.quit()
