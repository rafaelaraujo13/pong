import pygame

# iniciando pygame
try:
    pygame.init()
except:
    print('Erro ao carregar módulo Pygame')

# variáveis principais
rodando = True
branco = (255, 255, 255)
preto = (0, 0, 0)

# configurando tela
altura_tela = 480
comprimento_tela = 640
tela = pygame.display.set_mode((comprimento_tela, altura_tela))

# raquetes
def raquete(lado):
    if lado == 'esquerda':
        pygame.draw.rect(tela, preto, (0, (altura_tela / 2) - 50, 20, 100))
    elif lado == 'direita':
        pygame.draw.rect(tela, preto, (comprimento_tela - 20, (altura_tela / 2) - 50, 20, 100))

# loop do jogo
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    tela.fill(branco)
    
    # cria as raquetes
    raquete('esquerda')
    raquete('direita')
    
    
    pygame.display.update()