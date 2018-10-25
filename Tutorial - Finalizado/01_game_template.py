# -----------------------------------------------------------------------------
# 01_game_template.py
#
# Template básico para a criação de um jogo com a biblioteca ARCADE
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

import arcade
import os

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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
        
    # -------------------------------------------------------------------------
    # Inicia um novo jogo, configurando as variáveis
    # -------------------------------------------------------------------------
    def start_new_game(self):        
        pass
            
    # -------------------------------------------------------------------------
    # Renderiza os elementos na tela
    # -------------------------------------------------------------------------
    def on_draw(self):

        # Inicializa o renderizador da biblioteca Arcade
        arcade.start_render()
        
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
        pass
                    
                    
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
    
