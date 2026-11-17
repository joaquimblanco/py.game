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
        self.y = y
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