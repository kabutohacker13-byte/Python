# ================================================
# PROGRAMA: Tocando um MP3
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: DD/MM/YYYY
# VERSÃO: 1.0
# DESCRIÇÃO: toca musica em mp3
# ================================================
#FEITO COM AI
import pygame
import os
import random

# 1. Inicializa o Pygame e o Som
pygame.mixer.init()
pygame.init()

# 2. Configurações da Janela
LARGURA = 500
ALTURA = 350 # Aumentei um pouco para caber os botões
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tocador com Animação e Controles")

relogio = pygame.time.Clock()

# 3. Configuração do Arquivo (Mude para o nome da sua música!)
nome_arquivo = 'teste.mp3'

if not os.path.exists(nome_arquivo):
    print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
    rodando = False
else:
    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    rodando = True

# 4. Configurações da Animação (Equalizador)
quantidade_barras = 15
largura_barra = 20
espacamento = 10
x_inicial = (LARGURA - (quantidade_barras * (largura_barra + espacamento))) // 2

# Guardar as alturas para a animação não dar saltos bruscos se pausada
alturas_barras = [20] * quantidade_barras

# 5. Definição dos Botões (Posição X, Posição Y, Largura, Altura)
botao_pause = pygame.Rect(170, 290, 70, 35)
botao_play = pygame.Rect(260, 290, 70, 35)

# Configuração da Fonte para o texto dos botões
fonte = pygame.font.SysFont('Arial', 16, bold=True)

# Estado da música
musica_pausada = False

# 6. Loop Principal
while rodando:
    relogio.tick(30)
    tela.fill((20, 20, 20)) # Fundo escuro
    
    # Captura de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        # Detecta o clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: # Clique com o botão esquerdo
                pos_mouse = evento.pos
                
                # Se clicou no botão PAUSE
                if botao_pause.collidepoint(pos_mouse) and not musica_pausada:
                    pygame.mixer.music.pause()
                    musica_pausada = True
                    print("⏸️ Música pausada")
                    
                # Se clicou no botão PLAY
                elif botao_play.collidepoint(pos_mouse) and musica_pausada:
                    pygame.mixer.music.unpause()
                    musica_pausada = False
                    print("▶️ Música retomada")

    # --- DESENHO DO EQUALIZADOR ---
    if pygame.mixer.music.get_busy() and not musica_pausada:
        # Se estiver tocando, gera novas alturas aleatórias
        for i in range(quantidade_barras):
            alturas_barras[i] = random.randint(20, 180)

    # Desenha as barras na tela (Verde se tocando, Cinza se pausado)
    cor_barra = (57, 255, 20) if not musica_pausada else (80, 80, 80)
    for i in range(quantidade_barras):
        pos_x = x_inicial + i * (largura_barra + espacamento)
        pos_y = ALTURA - alturas_barras[i] - 90 # Ajustado para dar espaço aos botões
        pygame.draw.rect(tela, cor_barra, (pos_x, pos_y, largura_barra, alturas_barras[i]))

    # --- DESENHO DOS BOTÕES ---
    # Cores dinâmicas para os botões se adaptarem ao estado da música
    cor_btn_pause = (180, 50, 50) if not musica_pausada else (60, 60, 60)
    cor_btn_play = (50, 180, 50) if musica_pausada else (60, 60, 60)

    # Desenha os retângulos dos botões
    pygame.draw.rect(tela, cor_btn_pause, botao_pause, border_radius=5)
    pygame.draw.rect(tela, cor_btn_play, botao_play, border_radius=5)

    # Renderiza e centraliza o texto dentro dos botões
    txt_pause = fonte.render("PARAR", True, (255, 255, 255))
    txt_play = fonte.render("TOCA", True, (255, 255, 255))
    
    tela.blit(txt_pause, (botao_pause.x + 8, botao_pause.y + 8))
    tela.blit(txt_play, (botao_play.x + 15, botao_play.y + 8))

    # Se a música acabou completamente e não está pausada, fecha o programa
    if not pygame.mixer.music.get_busy() and not musica_pausada:
        rodando = False

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()


'''import pygame
import os

# 1. Inicializa o Pygame e o Mixer de Áudio
pygame.mixer.init()
pygame.init()

# 2. Configurações da Janela
largura = 400
altura = 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tocador de Música Pygame")

# 3. Definição de cores (RGB)
COR_FUNDO = (30, 30, 30)       # Cinza escuro
COR_TEXTO = (255, 255, 255)   # Branco

# 4. Configuração do arquivo de áudio (Mude para o nome do seu arquivo!)
nome_arquivo = 'teste.mp3' 

if not os.path.exists(nome_arquivo):
    print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
    rodando = False
else:
    try:
        pygame.mixer.music.load(nome_arquivo)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        print("🎵 Música tocando com janela aberta!")
        rodando = True
    except pygame.error as e:
        print(f"❌ Erro ao tocar: {e}")
        rodando = False

# 5. Loop Principal da Janela
while rodando:
    # Preenche o fundo da tela com a cor cinza
    tela.fill(COR_FUNDO)
    
    # Captura todos os eventos (como clicar no X para fechar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False # Sai do loop e fecha o programa

    # Atualiza a tela gráfica
    pygame.display.flip()

# Finaliza o Pygame e para a música ao fechar a janela
pygame.mixer.music.stop()
pygame.quit()'''


'''print('=' * 30)
print('Tocando um MP3'.upper().center(30))
print('=' * 30)

import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''import pygame
import os

# Inicializa o áudio
pygame.mixer.init()
pygame.init()

nome_arquivo = 'teste.mp3'

# Verifica se o arquivo realmente existe na pasta atual
if not os.path.exists(nome_arquivo):
    print(f"❌ ERRO: O arquivo '{nome_arquivo}' não foi encontrado nesta pasta!")
    print(f"Caminho atual do terminal: {os.getcwd()}")
else:
    try:
        pygame.mixer.music.load(nome_arquivo)
        
        # Garante que o volume do Pygame está no máximo (vai de 0.0 a 1.0)
        pygame.mixer.music.set_volume(1.0)
        
        pygame.mixer.music.play()
        print("🎵 Música iniciada com sucesso!")
        
        # Loop para monitorar o tempo
        segundos = 0
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1) # Espera 1 segundo
            segundos += 1
            print(f"Tempo tocando: {segundos}s...", end="\r")
            
    except pygame.error as e:
        print(f"❌ Erro ao reproduzir o áudio: {e}")'''