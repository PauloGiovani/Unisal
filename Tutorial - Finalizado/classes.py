# -----------------------------------------------------------------------------
# classes.py
#
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

# Classe Pokemon
class Pokemon(object):

    # Inicializador
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        
    # Exibe informações do pokemon
    def show_info(self):
        print(f"O pokemon se chama {self.nome} e é do tipo {self.tipo}.")
    
    
# Executa o programa
if __name__ == "__main__":
    
    # Cria dois pokemons
    pikachu = Pokemon("Pikachu", "Elétrico")
    charmander = Pokemon("Charmander", "Fogo")
    
    # Exibe informações dos pokemons
    pikachu.show_info()
    charmander.show_info()

