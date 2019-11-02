import pygame

# iniciando pygame
try:
    pygame.init()
except:
    print('Erro ao carregar módulo Pygame')

# variáveis principais
rodando = True
branco = (255, 255, 255)

# configurando tela
altura_tela = 480
comprimento_tela = 640
tela = pygame.display.set_mode((comprimento_tela, altura_tela))

# loop do jogo
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(branco)

    pygame.display.update()