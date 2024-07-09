# Exemplo de criação de tupla

livrosNicholasSparks = ("O desejo", "O retorno", "O melhor de mim","O milagre", "A última música", "A escolha", "Um porto seguro", "Um homem de sorte", "Diario de uma paixão", "Noites de tormenta", "O guardião","O milagre")

print(livrosNicholasSparks)

# Utilizando o método 'count' para contar a quantidade de vezes em que esse item se repete na tupla
print(livrosNicholasSparks.count("O milagre"))

# Utilizando o método 'index' para indicar o indice em que o item se localiza na tupla
print(livrosNicholasSparks.index("Noites de tormenta"))

# Utilizando funções na tupla
# ===========================

# Função 'len()' para contar a quantidade de itens possui a tupla

print(len(livrosNicholasSparks))

# Função 'max()' para retornar o item de maior valor da tupla

print(max(livrosNicholasSparks))

# Função 'min()' para retornar o item de menor valor da tupla

print(min(livrosNicholasSparks))

# Função 'sum()' para somar os valores de todos os itens da tupla
# Utilizado quando a tupla possui valores 'int' ou 'float'

tupla_number = (1, 2, 3, 4, 5.5)
print(sum(tupla_number))

# Função 'sorted()' para retornar a tupla ordenada

print(sorted(livrosNicholasSparks))