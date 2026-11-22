import pygame
pygame.init()
LARGURA = 960
ALTURA = 560
# cores
LARANJA = (232, 151, 66)
PRETO = (22, 21, 29)
BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Fase Maldita")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)
fonte_grande = pygame.font.Font(None, 96)
#FUNÇÕES 
def escrever(texto, qual_fonte, y, cor):
    # escreve um texto na tela
    imagem = qual_fonte.render(texto, True, cor)
    x = (LARGURA - imagem.get_width()) // 2
    tela.blit(imagem, (x, y))
#JOGO 
estado = "menu"          # "menu", "jogando", "nome" ou "fim"
rodando = True

while rodando:
    relogio.tick(60)   
    # TECLAS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:           
            rodando = False 
    #DESENHA
    if estado == "menu":
        tela.fill(PRETO)
        escrever("FASE MALDITA", fonte_grande, 60, LARANJA)
        escrever("Chegue na porta verde... se ela deixar.", fonte, 160, BRANCO)
    pygame.display.flip()           

pygame.quit()