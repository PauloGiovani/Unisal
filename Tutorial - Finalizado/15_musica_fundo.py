# -----------------------------------------------------------------------------
# 15_musica_fundo.py
#
# Insere a música de fundo
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

import arcade
import os
import random
import math
import pyglet

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

# -----------------------------------------------------------------------------
# Classe para a nave do jogador
# -----------------------------------------------------------------------------
class ShipSprite(arcade.Sprite):
    
    # Construtor, para configuração da nave do jogador
    def __init__(self, filename, scale):
        
        # Chama o construtor da classe pai
        super().__init__(filename, scale)
        
        # Posição inicial da nave do jogador
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 100
        
        # Controle do renascimento do jogador, após alguma colisão
        self.respawning = 0
        
    # -------------------------------------------------------------------------
    # Atualiza as informações da nave do jogador
    # -------------------------------------------------------------------------
    def update(self):
                
        # Controla o renascimento do jogador (transparência e velocidade)
        if self.respawning:
            
            # Aplica a transparência na nave do jogador
            self.respawning += 2
            self.alpha = self.respawning / 500.0
            
            # Remove a transparência da nave do jogador, após ele renascer
            if self.respawning > 250:
                self.respawning = 0 
                self.alpha = 1 
        
        # Atualiza a posição da nave do jogador
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Controle de verificação para os limites da tela
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
            
        # Chama o método update, presente na classe pai
        super().update()

# -----------------------------------------------------------------------------
# Classe para o tiro disparado pelo jogador
# -----------------------------------------------------------------------------
class BulletSprite(arcade.Sprite):
    
    # Construtor, para configuração do tiro disparado pelo jogador
    def __init__(self, filename, scale):
        
        # Chama o construtor da classe pai
        super().__init__(filename, scale)
        
    # Atualiza a posição do sprite do tiro disparado pelo jogador
    def update(self):
    
        # Atualiza a posição vertical do tiro disparado pelo jogador
        self.center_y += PLAYER_BULLET_SPEED
        
        # Remove o sprite do tiro, quando ele sair da tela
        if self.bottom > SCREEN_HEIGHT:
            self.kill()
        
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
# Classe para os inimigos
# -----------------------------------------------------------------------------
class EnemySprite(arcade.Sprite):
    
    # Construtor, para configuração da nuvem
    def __init__(self, filename, scale):
        
        # Chama o construtor da classe pai
        super().__init__(filename, scale)
        
    # Atualiza a posição do sprite do inimigo
    def update(self):
        
        # Atualiza a posição vertical do inimigo
        self.center_y += random.randint(-5, -1)
        
        # Remove o sprite do inimigo, quando ela sair da tela
        if self.top < 0:
            self.kill()
            
# -----------------------------------------------------------------------------
# Classe para o tiro disparado pelo inimigo
# -----------------------------------------------------------------------------
class EnemyBulletSprite(arcade.Sprite):
    
    # Construtor, para configuração do tiro disparado pelo inimigo
    def __init__(self, filename, scale):
        
        # Chama o construtor da classe pai
        super().__init__(filename, scale)
        
    # Atualiza a posição do sprite do tiro disparado pelo inimigo
    def update(self):
    
        # Atualiza a posição vertical do tiro do inimigo
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Remove o sprite do tiro, quando ele sair da tela
        if self.right < 0 or self.left > SCREEN_WIDTH or self.bottom > SCREEN_HEIGHT:
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
        
        # Carrega os sons
        self.gun_sound = arcade.sound.load_sound("sons/tiro_jogador.wav")
        self.laser_sound = arcade.sound.load_sound("sons/tiro_inimigo.wav")
        self.hit_sound = arcade.sound.load_sound("sons/acertou_inimigo.wav")
        self.collision_sound = arcade.sound.load_sound("sons/explosao.wav")
        self.laser_sound = arcade.sound.load_sound("sons/tiro_inimigo.wav")
        
        # Carrega e prepara o loop da música de fundo, utilizando o Pyglet (AVbin)
        self.src = pyglet.media.load("sons/musica_fundo_1.mp3")
        self.looper = pyglet.media.SourceGroup(self.src.audio_format, None)
        self.looper.loop = True
        self.looper.queue(self.src)
        
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
        
        # Pontuação do jogador
        self.score = 0
        
        # Carrega os dados do arquivo com a pontuação máxima do jogo       
        data = open(DATAFILE, 'r')
        self.record = data.read()
        data.close()
        
        # Listas com os sprites utilizados
        self.all_sprites_list = arcade.SpriteList(use_spatial_hash = False)
        self.enemies_list = arcade.SpriteList(use_spatial_hash = False)
        self.cloud_list = arcade.SpriteList(use_spatial_hash = False)
        self.player_list = arcade.SpriteList(use_spatial_hash = False)
        self.player_bullets_list = arcade.SpriteList(use_spatial_hash = False)
        self.enemies_bullets_list = arcade.SpriteList(use_spatial_hash = False)
        
        # Adiciona o sprite da nave do jogador
        self.player_sprite = ShipSprite("imagens/heroi.png", SHIP_SCALE)
        self.all_sprites_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite)
        
        # Configuração da música de fundo
        self.jukebox = pyglet.media.Player()
            
    # -------------------------------------------------------------------------
    # Renderiza os elementos na tela
    # -------------------------------------------------------------------------
    def on_draw(self):

        # Inicializa o renderizador da biblioteca Arcade
        arcade.start_render()
        
        # Se o jogador perdeu suas vidas, exibe a tela de GAME OVER
        if self.game_over:
            
            # Interrompe a música de fundo
            self.jukebox.pause()
            
            # Exibe a tela de Game Over
            self.draw_game_over()
            
        # Jogo normal
        else:
        
            # Renderiza os sprites (a ordem importa)
            self.cloud_list.draw()
            self.enemies_list.draw()
            self.player_list.draw()
            self.player_bullets_list.draw()
            self.enemies_bullets_list.draw()
            
            # Exibe o texto com o total de vidas do jogador
            output = f"Players: {self.lives}"
            arcade.draw_text(output, 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
            
            # Exibe o texto com a pontuação do jogador
            output = f"Score: {self.score}"
            arcade.draw_text(output, 200, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
            
            # Verifica se a pontuação do jogador superou o recorde do jogo
            if self.score > int(self.record):
                output = f"Record: {self.score}"
            else:
                output = f"Record: {self.record}"
                
            # Exibe o texto com o recorde de pontos do jogo
            arcade.draw_text(output, SCREEN_WIDTH - 185, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
            
            # Atualiza o som de fundo
            self.update_sound()
            
    # -------------------------------------------------------------------------
    # Permite atualizar a música de fundo, colocando-a em loop
    # -------------------------------------------------------------------------
    def update_sound(self):
        self.jukebox.queue(self.looper)
        self.jukebox.play()
        
    # -------------------------------------------------------------------------
    # Exibe o texto de GAME OVER
    # -------------------------------------------------------------------------
    def draw_game_over(self):
        
        # Texto Game Over
        output = "Game Over"
        arcade.draw_text(output, SCREEN_WIDTH / 2 - 220, SCREEN_HEIGHT / 2, arcade.color.WHITE, 72)
        
    # -------------------------------------------------------------------------
    # Controla as ações de acordo com a tecla que foi pressionada
    # -------------------------------------------------------------------------
    def on_key_press(self, key, key_modifiers):        
        
        # Movimenta a nave do jogador
        if key == arcade.key.UP:
            self.player_sprite.change_y = SHIP_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -SHIP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -SHIP_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = SHIP_SPEED
            
        # Dispara um tiro, quando o jogador pressionar a tecla SPACE
        elif key == arcade.key.SPACE:
        
            # Carrega o som do tiro do jogador
            arcade.sound.play_sound(self.gun_sound)
        
            # Carrega o sprite do tiro do jogador
            bullet_sprite = BulletSprite("imagens/tiro.png", PLAYER_BULLET_SCALE)
            
            # Define as coordenadas iniciais do sprite do tiro
            bullet_sprite.center_x = self.player_sprite.center_x
            bullet_sprite.bottom = self.player_sprite.top
            
            # Atualiza a posição do sprite do tiro
            bullet_sprite.update()
            
            # Insere o sprite do tiro na lista de todos os sprites
            self.all_sprites_list.append(bullet_sprite)

            # Adiciona o sprite do tiro na lista de tiros
            self.player_bullets_list.append(bullet_sprite)

    # -------------------------------------------------------------------------
    # Controla as ações de acordo com a tecla que foi liberada
    # -------------------------------------------------------------------------
    def on_key_release(self, key, key_modifiers):
        
        # Interrompe a movimentação da nave do jogador
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    
    # -------------------------------------------------------------------------
    # Atualiza a lógica do jogo, movendo todos os elementos da tela
    # -------------------------------------------------------------------------
    def update(self, delta_time):
        
        # Atualiza o contador de frames
        self.frame_count += 1
        
        # Se o jogo acabou
        if self.game_over:
            
            # Verifica se precisa atualizar o arquivo com a maior pontuação
            if self.score > int(self.record):
            
                # Abre o arquivo e sobrescreve seu conteúdo
                data = open(DATAFILE, 'w')
                data.write(str(self.score))
                data.close()
        
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
                    
            # -----------------------------------------------------------------
            # Inimigos
            # -----------------------------------------------------------------
            
            # Insere um inimigo a cada ENEMY_STEP frames e atualiza sua posição
            if self.frame_count % ENEMY_STEP == 0:
                
                # Carrega o sprite do inimigo
                enemy_sprite = EnemySprite("imagens/inimigo.png", ENEMY_SCALE)
                
                # Calcula a largura do inimigo
                enemy_width = int(enemy_sprite.width) // 2
                
                # Define a posição inicial do inimigo
                enemy_sprite.center_x = random.randint(enemy_width, SCREEN_WIDTH - enemy_width)
                enemy_sprite.center_y = SCREEN_HEIGHT + 100
                
                # Atualiza a posição do sprite do inimigo
                enemy_sprite.update()
                
                # Insere o sprite do inimigo na lista de todos os sprites
                self.all_sprites_list.append(enemy_sprite)
                
                # Adiciona o inimigo na lista de inimigos
                self.enemies_list.append(enemy_sprite)
                    
            # -----------------------------------------------------------------
            # Verifica a colisão do tiro do player com os inimigos
            # -----------------------------------------------------------------

            # Para cada tiro disparado pelo jogador
            for bullet in self.player_bullets_list:

                # Verifica se o tiro acertou a nave do inimigo
                hit_list = arcade.check_for_collision_with_list(bullet, self.enemies_list)

                # Se acertou, remove o tiro da tela
                if len(hit_list) > 0:
                    bullet.kill()

                # Para cada inimigo que o tiro acertou
                for enemy in hit_list:
                    
                    # Remove o inimigo da tela
                    enemy.kill()
                    
                    # Atualiza a pontuação do jogador
                    self.score += POINTS
                    
                    # Som do acerto
                    arcade.sound.play_sound(self.hit_sound)
                    
            # -----------------------------------------------------------------
            # Verifica a colisão do inimigo com a nave do jogador
            # -----------------------------------------------------------------

            # Para cada inimigo
            for enemy in self.enemies_list:

                # Verifica se inimigo colidiu com a nave do jogador
                hit_list = arcade.check_for_collision_with_list(enemy, self.player_list)

                # Se acertou, remove o inimigo da tela
                if len(hit_list) > 0:
                    enemy.kill()

                # Para cada colisão entre a nave do inimigo e a nave do jogador
                for player in hit_list:
                    
                    # Retira uma vida do jogador
                    self.lives -= 1
                    
                    # Indica que o jogador está renascendo
                    player.respawning = 1
                    
                    # Som da colisão
                    arcade.sound.play_sound(self.collision_sound)
                    
                # Controla o disparo do inimigo, quando ele estiver a 
                # ENEMY_BULLET_POSITION do final da tela
                if enemy.center_y < ENEMY_BULLET_POSITION:
                                       
                    # O tiro do inimigo é disparado a cada ENEMY_BULLET_STEP frames
                    if self.frame_count % ENEMY_BULLET_STEP == 0:
                    
                        # Carrega o som do tiro
                        arcade.sound.play_sound(self.laser_sound)
                        
                        # Carrega o sprite do tiro
                        enemy_bullet_sprite = EnemyBulletSprite("imagens/missile.png", ENEMY_BULLET_SCALE)
                        
                        # Define as coordenadas iniciais do sprite do tiro
                        enemy_bullet_sprite.center_x = enemy.center_x
                        enemy_bullet_sprite.bottom = enemy.top
                        
                        # Posição inicial do tiro
                        start_x = enemy.center_x
                        start_y = enemy.center_y

                        # Destino do tiro
                        dest_x = self.player_sprite.center_x
                        dest_y = self.player_sprite.center_y
                        
                        # Calcula o ângulo para rotacionar o tiro do inimigo
                        x_diff = dest_x - start_x
                        y_diff = dest_y - start_y
                        angle = math.atan2(y_diff, x_diff)
                        
                        # Transforma em graus
                        enemy_bullet_sprite.angle = math.degrees(angle) - 90
                        
                        # Rotaciona o sprite do tiro
                        enemy_bullet_sprite.change_x = math.cos(angle) * ENEMY_BULLET_SPEED
                        enemy_bullet_sprite.change_y = math.sin(angle) * ENEMY_BULLET_SPEED
                        
                        # Atualiza a posição do sprite do tiro
                        enemy_bullet_sprite.update()
                        
                        # Insere o sprite do tiro na lista de todos os sprites
                        self.all_sprites_list.append(enemy_bullet_sprite)

                        # Adiciona o sprite do tiro na lista de tiros
                        self.enemies_bullets_list.append(enemy_bullet_sprite)
                        
                # -------------------------------------------------------------
                # Verifica a colisão dos tiros do inimigo com a nave do jogador
                # -------------------------------------------------------------

                # Para cada tiro do inimigo
                for bullet in self.enemies_bullets_list:

                    # Verifica se inimigo colidiu com a nave do jogador
                    hit_list = arcade.check_for_collision_with_list(bullet, self.player_list)

                    # Se acertou, remove o inimigo da tela
                    if len(hit_list) > 0:
                        bullet.kill()

                    # Para cada colisão entre a nave do inimigo e a nave do jogador
                    for player in hit_list:
                        
                        # Retira uma vida do jogador
                        self.lives -= 1
                        
                        # Indica que o jogador está renascendo
                        player.respawning = 1
                        
                        # Som da colisão
                        arcade.sound.play_sound(self.collision_sound)
                    
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
    
