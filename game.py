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
pos_usu = (altura_tela / 2) - 50
vel = 0

# config da raquete do computador
pos_comp = (altura_tela / 2) - 50
vel_comp = 10

# colisão das raquetes com a borda do jogo
def jogador_esta_colidindo():
    if pos_usu == 0 or pos_usu + tam == altura_tela:
        return True
    else:
        return False

def computador_esta_colidindo():
    if pos_comp == 0 or pos_comp + tam == altura_tela:
        return True
    else:
        return False
       

# criar raquetes
def raquete(lado):
    if lado == 'esquerda':
        pygame.draw.rect(tela, preto, (0, pos_usu, 20, tam))
    elif lado == 'direita':
        pygame.draw.rect(tela, preto, (comprimento_tela - 20, pos_comp, 20, tam))

# loop do jogo
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if vel != 0:
                    vel = vel * -1
                else:
                    vel = 10

    tela.fill(branco)
    
    # checa se chegaram na borda

    if jogador_esta_colidindo():
        vel = vel * -1

    if computador_esta_colidindo():
        vel_comp = vel_comp * -1

    # faz as raquetes andarem

    pos_comp += vel_comp
    pos_usu += vel

    # cria as raquetes

    raquete('esquerda')
    raquete('direita')
    print(jogador_esta_colidindo())
    
    # atualiza a tela
    pygame.display.update()
    clock.tick(30)