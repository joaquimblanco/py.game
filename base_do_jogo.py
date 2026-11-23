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
        self.y = y
        self.velocidade_y = 0
        self.no_chao = False
    def mover(self, deslocamento_x, deslocamento_y):
        self.x += deslocamento_x
        self.y += deslocamento_y
    def pular(self):
        if self.no_chao:
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
zerou = False
nome = ""
ranking = []
rodando = True
while rodando:
    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
            if estado == "menu":
                if evento.key == pygame.K_RETURN:
                    fase = 0
                    estado = "jogando"
                    comecar_fase = True
                    mortes = 0
                    quadros = 0
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif evento.unicode.isalpha() and len(nome) < 3:
                    nome = nome + evento.unicode.upper()
            elif estado == "jogando":
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_w or evento.key == pygame.K_UP:
                    if posicao_quadrado.no_chao and tem_som:
                        som_pulo.play()
                    posicao_quadrado.pular()
    if comecar_fase:
        comecar_fase = False
        blocos = []
        espinhos = []
        falsos = []
        invisiveis = []
        revelados = []
        caem = []
        caindo = []
        escondidos = []
        portas_falsas = []
        teleportes = []
        inversores = []
        invertido = False
        porta_foge = False
        porta_fugindo = False
        mapa = mapas[fase]
        for linha in range(len(mapa)):
            for coluna in range(len(mapa[linha])):
                letra = mapa[linha][coluna]
                x = coluna * TAM
                y = linha * TAM
                if letra == "#" or letra == "X" or letra == "I":
                    blocos.append(pygame.Rect(x, y, TAM, TAM))
                    if letra == "X":
                        falsos.append(pygame.Rect(x, y, TAM, TAM))
                    if letra == "I":
                        invisiveis.append(pygame.Rect(x, y, TAM, TAM))
                elif letra == "^":
                    espinhos.append(pygame.Rect(x, y + 20, TAM, 20))
                elif letra == "D":
                    porta = pygame.Rect(x + 8, y, 24, TAM)
                elif letra == "P":
                    posicao_quadrado = quadrado("preto", x, y)
                    inicio_x = x
                    inicio_y = y
                elif letra == "F":
                    caem.append(pygame.Rect(x, y, TAM, TAM))
                elif letra == "H":
                    escondidos.append(pygame.Rect(x, y, TAM, TAM))
                elif letra == "E":
                    portas_falsas.append(pygame.Rect(x + 8, y, 24, TAM))
                elif letra == "T":
                    teleportes.append(pygame.Rect(x, y + 20, TAM, 20))
                elif letra == "C":
                    inversores.append(pygame.Rect(x, y + 20, TAM, 20))
                elif letra == "d":
                    porta_foge = True
                    destino_x = x + 8
    if estado == "jogando":
        quadros += 1
        teclas = pygame.key.get_pressed()
        velocidade_x = 0
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            velocidade_x = VELOCIDADE
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            velocidade_x = -VELOCIDADE
        if invertido:
            velocidade_x = -velocidade_x
        posicao_quadrado.mover(velocidade_x, 0)
        caixa = pygame.Rect(posicao_quadrado.x, posicao_quadrado.y, TAM, TAM)
        for bloco in blocos:
            if caixa.colliderect(bloco):
                if velocidade_x > 0:
                    posicao_quadrado.x = bloco.left - TAM
                if velocidade_x < 0:
                    posicao_quadrado.x = bloco.right
                caixa.x = posicao_quadrado.x
        posicao_quadrado.velocidade_y += GRAVIDADE
        posicao_quadrado.mover(0, int(posicao_quadrado.velocidade_y))
        caixa.y = posicao_quadrado.y
        for bloco in blocos:
            if caixa.colliderect(bloco):
                if posicao_quadrado.velocidade_y > 0:
                    posicao_quadrado.y = bloco.top - TAM
                else:
                    posicao_quadrado.y = bloco.bottom
                posicao_quadrado.velocidade_y = 0
                caixa.y = posicao_quadrado.y
        pes = caixa.move(0, 1)
        posicao_quadrado.no_chao = False
        for bloco in blocos:
            if pes.colliderect(bloco):
                posicao_quadrado.no_chao = True
        for falso in falsos:
            gatilho = pygame.Rect(falso.x, falso.y - 2, TAM, 2)
            if caixa.colliderect(gatilho) and falso in blocos:
                blocos.remove(falso)
        for invisivel in invisiveis:
            gatilho = pygame.Rect(invisivel.x - 1, invisivel.y - 1, TAM + 2, TAM + 2)
            if caixa.colliderect(gatilho) and invisivel not in revelados:
                revelados.append(invisivel)
        for cai in caem:
            gatilho = pygame.Rect(cai.x - TAM, cai.bottom, 3 * TAM, ALTURA)
            if caixa.colliderect(gatilho) and cai not in caindo:
                caindo.append(cai)
        for cai in caindo:
            if cai.y < ALTURA:
                cai.y += 8
            if caixa.colliderect(cai):
                comecar_fase = True
        for escondido in escondidos:
            gatilho = pygame.Rect(escondido.x - 2 * TAM, escondido.y, 5 * TAM, TAM)
            espinho_novo = pygame.Rect(escondido.x, escondido.y + 20, TAM, 20)
            if caixa.colliderect(gatilho) and espinho_novo not in espinhos:
                espinhos.append(espinho_novo)
        for porta_falsa in portas_falsas:
            if caixa.colliderect(porta_falsa):
                comecar_fase = True
        for teleporte in teleportes:
            if caixa.colliderect(teleporte):
                posicao_quadrado.x = inicio_x
                posicao_quadrado.y = inicio_y
                posicao_quadrado.velocidade_y = 0
                caixa.x = inicio_x
                caixa.y = inicio_y
        for inversor in inversores:
            if caixa.colliderect(inversor):
                invertido = True
        if porta_foge:
            if porta.x - posicao_quadrado.x < 100:
                porta_fugindo = True
            if porta_fugindo and porta.x < destino_x:
                porta.x += 6
                if porta.x > destino_x:
                    porta.x = destino_x
        for espinho in espinhos:
            if caixa.colliderect(espinho):
                comecar_fase = True
        if posicao_quadrado.y > ALTURA:
            comecar_fase = True
        if comecar_fase:
            mortes += 1
        if comecar_fase and tem_som:
            som_morte.play()
        if caixa.colliderect(porta):
            if tem_som:
                som_porta.play()
            fase += 1
            if fase < len(mapas):
                comecar_fase = True
            else:
                estado = "menu"
                zerou = True
                tempo = round(quadros / 60, 1)
                if nome == "":
                    nome = "???"
                ranking.append([mortes, tempo, nome])
                ranking.sort()
                ranking = ranking[:5]
                nome = ""
    if estado == "menu":
        tela.fill(PRETO)
        escrever("FASE MALDITA", fonte_grande, 60, LARANJA)
        escrever("Chegue na porta verde... se ela deixar.", fonte, 160, BRANCO)
        escrever("Aperte ENTER para começar", fonte, 260, LARANJA)
        if zerou:
            escrever(f"VOCÊ ZEROU!   Mortes: {mortes}   Tempo: {tempo}s", fonte, 205, VERDE)
        escrever("Seu nome (3 letras): " + nome + "_", fonte, 305, BRANCO)
        escrever("MELHORES PARTIDAS", fonte, 350, LARANJA)
        if len(ranking) == 0:
            escrever("Ninguém zerou ainda.", fonte, 390, BRANCO)
        posicao = 1
        for partida in ranking[:3]:
            escrever(f"{posicao}. {partida[2]}   {partida[0]} mortes   {partida[1]}s", fonte, 350 + posicao * 40, BRANCO)
            posicao += 1
    elif estado == "jogando":
        tela.fill(LARANJA)
        for bloco in blocos:
            desenhar_bloco(bloco)
        for espinho in espinhos:
            desenhar_espinho(espinho)
        desenhar_porta(porta)
        for invisivel in invisiveis:
            if invisivel not in revelados:
                pygame.draw.rect(tela, LARANJA, invisivel)
                if abs(posicao_quadrado.x - invisivel.x) < 68 and abs(posicao_quadrado.y - invisivel.y) < 96:
                    pygame.draw.rect(tela, BRANCO, (invisivel.x + 2, invisivel.y + 2, TAM - 4, TAM - 4), 2)
        for cai in caem:
            desenhar_bloco(cai)
        for porta_falsa in portas_falsas:
            desenhar_porta(porta_falsa)
        pygame.draw.rect(tela, PRETO, (posicao_quadrado.x, posicao_quadrado.y, TAM, TAM))
        if invertido:
            pygame.draw.rect(tela, VERMELHO, (posicao_quadrado.x + 10, posicao_quadrado.y + 10, 20, 20))
        pygame.draw.rect(tela, PRETO, (0, 0, LARGURA, 40))
        placar = f"Fase {fase + 1}/{len(mapas)}   Mortes: {mortes}   Tempo: {quadros // 60}s"
        tela.blit(fonte.render(placar, True, BRANCO), (16, 8))
    pygame.display.flip()
pygame.quit()