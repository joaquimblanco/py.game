import pygame
pygame.init()
tela = pygame.display.set_mode((960, 560))
class quadrado:
    def __init__(self, nome, x):
        self.nome = nome
        self.x = x
    def mover(self, deslocamento):
        self.x += deslocamento
posicao_quadrado = quadrado("preto", 100)
pygame.display.set_caption("Fase malidita")
timer = pygame.time.Clock()
rodando = True
while rodando:  
    timer.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    teclas = pygame.key.get_pressed()
    velocidade = 0
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        velocidade = 3
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            velocidade = -3
    posicao_quadrado.mover(velocidade)
    if posicao_quadrado.x > 960:
        posicao_quadrado.x = -40
    if posicao_quadrado.x < -40:
            posicao_quadrado.x = 960
    tela.fill((232, 151, 66))
    pygame.draw.rect(tela, (0, 0, 0), (posicao_quadrado.x, 300, 40, 40))
    pygame.display.flip()
pygame.quit()
