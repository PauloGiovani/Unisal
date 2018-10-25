# -----------------------------------------------------------------------------
# conceitos_basicos.py
#
# Autor: Paulo Giovani
# Data: 20/08/2018
# Atualização: 01/10/2018
# -----------------------------------------------------------------------------

# Define algumas variáveis
a = 10
nome = 'Paulo'
valor = 1.99

# Exibe os valores
print("A: %d" %a)
print("Nome: {}".format(nome))
print(f"Valor: {valor}")

# Define uma lista de valores
itens = ['Espada', 'Magia', 'Suco']

# Pula uma linha
print()

# Exibe os itens utilizando um laço FOR
for item in itens:
    print(item)
    
# Pula uma linha
print()
    
# Entrada e exibição de um valor
numero = int(input("Informe o número: "))

print("Você digitou: %d\n" %numero)
