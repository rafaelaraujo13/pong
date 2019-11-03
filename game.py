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
tam = 80
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
    c = -10
    if lado == 'esquerda':
        for i in range(0, int(tam / 10)):
            c += 10
            pygame.draw.rect(tela, branco, (0, pos_usu + c, 20, 10))

    elif lado == 'direita':
        for i in range(0, int(tam / 10)):
            c += 10
            pygame.draw.rect(tela, branco, (comprimento_tela - 20, pos_comp + c, 20, 10))


# configurações da bola
velx_bola = -10
vely_bola = 0
posx_bola = (comprimento_tela / 2)
posy_bola = (altura_tela / 2)

# criar bola
def bola():
    pygame.draw.rect(tela, branco, (posx_bola, posy_bola, 10, 10))
    
# colisão da bola com as raquetes
def bola_na_raquete():
    if posx_bola == 20 or posx_bola == comprimento_tela - 20:
        if posy_bola in range(int(pos_usu), int(pos_usu + 100)):
            return True
    else:
        return False

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

    tela.fill(preto)
    
    # checa se as raquetes chegaram na borda ou a bolinha bateu nelas

    if jogador_esta_colidindo():
        vel = vel * -1

    if computador_esta_colidindo():
        vel_comp = vel_comp * -1

    if bola_na_raquete():
        velx_bola = velx_bola * -1

    # faz as raquetes e bola andarem

    pos_comp += vel_comp
    pos_usu += vel
    posx_bola += velx_bola
    posy_bola += vely_bola

    # cria as raquetes e bola

    raquete('esquerda')
    raquete('direita')
    bola()

    print(pos_usu, posx_bola)

    # atualiza a tela
    pygame.display.update()
    clock.tick(30)