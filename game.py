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
    if lado == 'esquerda':
        pygame.draw.rect(tela, branco, (0, pos_usu, 20, tam))

    elif lado == 'direita':
        pygame.draw.rect(tela, branco, (comprimento_tela - 20, pos_comp, 20, tam))


# configurações da bola
velx_bola = -10
vely_bola = 0
posx_bola = (comprimento_tela / 2) 
posy_bola = (altura_tela / 2)
bola_rebatida = False

# criar bola
def bola():
    pygame.draw.rect(tela, branco, (posx_bola, posy_bola, 10, 10))
    
# colisão da bola com as raquetes
def bola_na_raquete():
    if posx_bola == 20:
        return 'jogador'
    elif posx_bola == comprimento_tela - 20:
        return 'computador'
    else:
        return False

# define velocidades x e y da bola
def definir_velocidade_bola(lado):
    global velx_bola, vely_bola

    if lado == 'jogador':
        if posy_bola >= pos_usu and posy_bola < pos_usu + 10:
            velx_bola = velx_bola * -1
            vely_bola = -5
        elif posy_bola >= pos_usu + 10 and posy_bola < pos_usu + 20:
            velx_bola = velx_bola * -1
            vely_bola = -4
        elif posy_bola >= pos_usu + 20 and posy_bola < pos_usu + 30:
            velx_bola = velx_bola * -1
            vely_bola = -3
        elif posy_bola >= pos_usu + 30 and posy_bola < pos_usu + 40:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_usu + 40 and posy_bola < pos_usu + 50:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_usu + 50 and posy_bola < pos_usu + 60:
            velx_bola = velx_bola * -1
            vely_bola = 3
        elif posy_bola >= pos_usu + 60 and posy_bola < pos_usu + 70:
            velx_bola = velx_bola * -1
            vely_bola = 4
        elif posy_bola >= pos_usu + 70 and posy_bola < pos_usu + 80:
            velx_bola = velx_bola * -1
            vely_bola = 5
        
    elif lado == 'computador':
        if posy_bola >= pos_comp and posy_bola < pos_comp + 10:
            velx_bola = velx_bola * -1
            vely_bola = -5
        elif posy_bola >= pos_comp + 10 and posy_bola < pos_comp + 20:
            velx_bola = velx_bola * -1
            vely_bola = -4
        elif posy_bola >= pos_comp + 20 and posy_bola < pos_comp + 30:
            velx_bola = velx_bola * -1
            vely_bola = -3
        elif posy_bola >= pos_comp + 30 and posy_bola < pos_comp + 40:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_comp + 40 and posy_bola < pos_comp + 50:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_comp + 50 and posy_bola < pos_comp + 60:
            velx_bola = velx_bola * -1
            vely_bola = 3
        elif posy_bola >= pos_comp + 60 and posy_bola < pos_comp + 70:
            velx_bola = velx_bola * -1
            vely_bola = 4
        elif posy_bola >= pos_comp + 70 and posy_bola < pos_comp + 80:
            velx_bola = velx_bola * -1
            vely_bola = 5

# colisão da bola com as bordas do jogo
def bola_esta_colidindo():
    if posy_bola == 0 or posy_bola + 10 == altura_tela:
        return True
    else:
        return False

# ponto
def pontuou():
    if posx_bola == 0:
        return 'computador'
    elif posx_bola + 10 == comprimento_tela:
        return 'jogador'
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

    colisao = bola_na_raquete()

    # muda a velocidade da bolinha

    if colisao != False:
        definir_velocidade_bola(colisao)

    # checa se a bolinha bateu na borda e muda sua direção

    if bola_esta_colidindo():
        vely_bola = vely_bola * -1

    # checa se foi gol

    ganhador = pontuou()
    if ganhador != False:
        print(ganhador + ' ganhou!!!!')
        rodando = False

    # faz as raquetes e bola andarem

    pos_comp += vel_comp
    pos_usu += vel
    posx_bola += velx_bola
    posy_bola += vely_bola

    # cria as raquetes e bola

    raquete('esquerda')
    raquete('direita') 
    bola()

    # atualiza a tela
    pygame.display.update()
    clock.tick(30)