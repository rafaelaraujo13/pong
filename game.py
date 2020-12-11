import pygame
from random import randint, choice
from time import sleep

# iniciando pygame
try:
    pygame.init()
    pygame.font.init()
except:
    print('Erro ao carregar módulo Pygame')

# configurando tela
altura_tela = 480
comprimento_tela = 640
tela = pygame.display.set_mode((comprimento_tela, altura_tela))

# variáveis principais
rodando = True
branco = (255, 255, 255)
preto = (0, 0, 0)
clock = pygame.time.Clock()
fonte = pygame.font.get_default_font()
fonte_placar = pygame.font.SysFont(fonte, 45)
msg = '0 x 0'
text = fonte_placar.render(msg, True, branco)
text_rect = text.get_rect()
text_rect.center = (comprimento_tela / 2, 30)



# config do jogo
pontos_jog = 0
pontos_comp = 0


# config da raquete do jogador
tam = 120
pos_usu = (altura_tela / 2) - 50
vel = 0

# config da raquete do computador
pos_comp = (altura_tela / 2) - 50
vel_comp = 10

# configurações da bola
velx_bola = -10
vely_bola = choice([0, 5, -5])
posx_bola = (comprimento_tela / 2) 
posy_bola = (altura_tela / 2)
bola_rebatida = False

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

# controla os movimentos da raquete do computador (seguindo a bolinha)
def comp_vai_mexer():
    if not computador_esta_colidindo():
        posicao_que_a_bola_vai_bater = randint(0, tam)
        if posx_bola > comprimento_tela / 2:
            if posy_bola > pos_comp + posicao_que_a_bola_vai_bater:
                if vel_comp != 10:
                    return True
            else:
                if vel_comp != -10:
                    return True

    return False

# criar bola
def bola():
    pygame.draw.rect(tela, branco, (posx_bola, posy_bola, 10, 10))
    
# colisão da bola com as raquetes
def bola_na_raquete():
    if posx_bola == 20:
        return 'jogador'
    elif posx_bola + 10 == comprimento_tela - 20:
        return 'computador'
    else:
        return False

# define velocidades x e y da bola
def definir_velocidade_bola(lado):
    global velx_bola, vely_bola

    if lado == 'jogador':
        if posy_bola >= pos_usu and posy_bola < pos_usu + 40:
            velx_bola = velx_bola * -1
            vely_bola = -5
        elif posy_bola >= pos_usu + 40 and posy_bola < pos_usu + 80:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_usu + 80 and posy_bola < pos_usu + 120:
            velx_bola = velx_bola * -1
            vely_bola = 5
        
    elif lado == 'computador':
        if posy_bola >= pos_comp and posy_bola < pos_comp + 40:
            velx_bola = velx_bola * -1
            vely_bola = -5
        elif posy_bola >= pos_comp + 40 and posy_bola < pos_comp + 80:
            velx_bola = velx_bola * -1
            vely_bola = 0
        elif posy_bola >= pos_comp + 80 and posy_bola < pos_comp + 120:
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
                if vel != 0 and not jogador_esta_colidindo():
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


    # controla o movimento da raquete do computador
    if comp_vai_mexer():
        vel_comp = vel_comp * -1


    # muda a velocidade da bolinha

    if colisao != False:
        definir_velocidade_bola(colisao)

    # checa se a bolinha bateu na borda e muda sua direção

    if bola_esta_colidindo():
        vely_bola = vely_bola * -1

    # checa se foi gol

    pontuador = pontuou()
    if pontuador != False:
        
        if pontuador == 'jogador':
            pontos_jog = pontos_jog + 1
        elif pontuador == 'computador':
            pontos_comp = pontos_comp + 1
        
        print(f'Jogador: {pontos_jog}')
        print(f'Computador: {pontos_comp}')
        posx_bola = comprimento_tela / 2
        posy_bola = altura_tela / 2
        vely_bola = choice([5, -5])
        velx_bola = choice([10, -10])
        vel = 0
        pos_comp = (altura_tela / 2) - 50
        pos_usu = (altura_tela / 2) - 50

        
        msg = f'{pontos_jog} x {pontos_comp}'
        text = fonte_placar.render(msg, True, branco)

    # faz as raquetes e bola andarem

    pos_comp += vel_comp
    pos_usu += vel
    posx_bola += velx_bola
    posy_bola += vely_bola

    # cria as raquetes e bola

    raquete('esquerda')
    raquete('direita') 
    bola()

    # placar

    tela.blit(text, text_rect)

    # atualiza a tela
    pygame.display.update()
    clock.tick(30)