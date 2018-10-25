# -----------------------------------------------------------------------------
# game_config.py
#
# Arquivo de configuração do jogo
# Autor: Paulo Giovani
# Data: 20/08/2018
# Last update: 01/10/2018
# -----------------------------------------------------------------------------

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Intervalo para inserir as nuvens
CLOUD_STEP = 200

# Constantes utilizadas pelo jogador
PLAYER_LIVES = 3
SHIP_SCALE = 1.0
SHIP_SPEED = 2.0
PLAYER_BULLET_SCALE = 1.0
PLAYER_BULLET_SPEED = 5.0

# Intervalo para inserir os inimigos
ENEMY_STEP = 90

# Constantes utilizadas pelos inimigos
ENEMY_SCALE = 1.0
ENEMY_BULLET_STEP = 80
ENEMY_BULLET_POSITION = 400
ENEMY_BULLET_SCALE = 1.0
ENEMY_BULLET_SPEED = 4.0

# Valor a ser somado para a pontuação do jogador
POINTS = 100

# Nome do arquivo com a pontuação máxima do jogo
DATAFILE = 'record.txt'