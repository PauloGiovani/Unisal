# -----------------------------------------------------------------------------
# 02_nuvens.py
#
# Insere as nuvens
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

import arcade
import os
import random

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Intervalo para inserir as nuvens
CLOUD_STEP = 200

# Constantes utilizadas pelo jogador
PLAYER_LIVES = 3

# -----------------------------------------------------------------------------
# Classe para as nuvens
# -----------------------------------------------------------------------------
class CloudSprite(arcade.Sprite):
    
    # Construtor, para configuração da nuvem
    def __init__(self, filename, scale):
        
        # Chama o construtor da classe pai
        super().__init__(filename, scale)
        
    # Atualiza a posição do sprite da nuvem
    def update(self):
        
        # Atualiza a posição vertical da nuvem
        self.center_y += random.randint(-2, -1)
        
        # Remove o sprite da nuvem, quando ela sair da tela
        if self.top < 0:
            self.kill()

# -----------------------------------------------------------------------------
# Classe principal
# -----------------------------------------------------------------------------
class MyGame(arcade.Window):

    # Construtor principal
    def __init__(self, width, height):
    
        # Inicializa a classe pai
        super().__init__(width, height, "Shooter Tutorial 1.0")
        
        # Define uma cor de fundo
        arcade.set_background_color((160, 212, 235))
        
        # Diretório com os arquivos
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
    # -------------------------------------------------------------------------
    # Inicia um novo jogo, configurando as variáveis variáveis
    # -------------------------------------------------------------------------
    def start_new_game(self):
    
        # Contador de frames
        self.frame_count = 0
        
        # Estado do jogo
        self.game_over = False
        
        # Total inicial de vidas do jogador
        self.lives = PLAYER_LIVES
        
        # Listas com os sprites utilizados
        self.all_sprites_list = arcade.SpriteList(use_spatial_hash = False)
        self.cloud_list = arcade.SpriteList(use_spatial_hash = False)
            
    # -------------------------------------------------------------------------
    # Renderiza os elementos na tela
    # -------------------------------------------------------------------------
    def on_draw(self):

        # Inicializa o renderizador da biblioteca Arcade
        arcade.start_render()
        
        # Se o jogador perdeu suas vidas, exibe a tela de GAME OVER
        if self.game_over:
            pass
            
        # Jogo normal
        else:
        
            # Renderiza os sprites (a ordem importa)
            self.cloud_list.draw()
        
    # -------------------------------------------------------------------------
    # Controla as ações de acordo com a tecla que foi pressionada
    # -------------------------------------------------------------------------
    def on_key_press(self, key, key_modifiers):        
        pass

    # -------------------------------------------------------------------------
    # Controla as ações de acordo com a tecla que foi liberada
    # -------------------------------------------------------------------------
    def on_key_release(self, key, key_modifiers):
        pass
    
    # -------------------------------------------------------------------------
    # Atualiza a lógica do jogo, movendo todos os elementos da tela
    # -------------------------------------------------------------------------
    def update(self, delta_time):
        
        # Atualiza o contador de frames
        self.frame_count += 1
        
        # Se o jogo acabou
        if self.game_over:
            pass
        
        # Se o jogador ainda não morreu
        if not self.game_over:
            
            # Atualiza todos os sprites do jogo
            self.all_sprites_list.update()
            
            # Verifica se o jogador perdeu todas as suas vidas
            if self.lives < 0:
                self.game_over = True
            
            # -----------------------------------------------------------------
            # Nuvens
            # -----------------------------------------------------------------
            
            # Insere uma nuvem a cada CLOUD_STEP frames e atualiza sua posição
            if self.frame_count % CLOUD_STEP == 0:
                
                # Define um fator para redimensionar a nuvem
                fator = random.uniform(0.1, 0.4)
                
                # Carrega o sprite redimensionado da nuvem
                cloud_sprite = CloudSprite("imagens/nuvem.png", fator)
                
                # Calcula a largura da nuvem
                cloud_width = int(cloud_sprite.width) // 2
                
                # Define a posição inicial da nuvem
                cloud_sprite.center_x = random.randint(cloud_width, SCREEN_WIDTH - cloud_width)
                cloud_sprite.center_y = SCREEN_HEIGHT + 100
                
                # Atualiza a posição do sprite da nuvem
                cloud_sprite.update()
                
                # Insere o sprite da nuvem na lista de todos os sprites
                self.all_sprites_list.append(cloud_sprite)

                # Adiciona o sprite da nuvem na lista de nuvens
                self.cloud_list.append(cloud_sprite)
                    
                    
# -----------------------------------------------------------------------------
# Método principal
# -----------------------------------------------------------------------------
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.start_new_game()
    arcade.run()
    
# -----------------------------------------------------------------------------
# Executa o método principal
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    
