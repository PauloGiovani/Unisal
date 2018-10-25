# -----------------------------------------------------------------------------
# funcoes.py
#
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

# Define uma função que retorna o maior valor
def maior_valor(a, b):
    
    # Estrutura de decisão
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "ambos são iguais!"
    
    
# Executa o programa
if __name__ == "__main__":
    
    # Entrada dos valores
    a = int(input("Informe o valor 1: "))
    b = int(input("Informe o valor 2: "))
    
    # Chama a função para encontrar o maior valor
    maior = maior_valor(a, b)
    
    # Exibe o resultado
    print("\nMaior valor: %s" %maior)

