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
clock = pygame.time.Clock()

# configurando tela
altura_tela = 480
comprimento_tela = 640
tela = pygame.display.set_mode((comprimento_tela, altura_tela))

# config da raquete do jogador
tam = 100
pos_y = (altura_tela / 2) - 50
vel = 0

# colisão da raquete com a borda do jogo
def esta_colidindo():
    if pos_y == 0 or pos_y + tam == altura_tela:
        return True
    else:
        return False
       

# criar raquetes
def raquete(lado):
    if lado == 'esquerda':
        pygame.draw.rect(tela, preto, (0, pos_y, 20, tam))
    elif lado == 'direita':
        pygame.draw.rect(tela, preto, (comprimento_tela - 20, (altura_tela / 2) - 50, 20, tam))

# loop do jogo
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if vel == 0:
                    vel = 10
                else:
                    vel = vel * -1
    
    tela.fill(branco)
    
    # cria as raquetes

    if esta_colidindo():
        vel = vel * -1

    pos_y += vel

    raquete('esquerda')
    raquete('direita')
    
    
    pygame.display.update()
    clock.tick(30)