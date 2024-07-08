# Exemplo de criação de lista

livrosNicholasSparks = ["O desejo", "O retorno", "O melhor de mim","O milagre", "A última música", "A escolha", "Um porto seguro", "Um homem de sorte", "Diario de uma paixão", "Noites de tormenta", "O guardião"]
print(livrosNicholasSparks)
print(type(livrosNicholasSparks))

# Adicionando um item à lista

livrosNicholasSparks.append("Um amor para recordar")
print(livrosNicholasSparks)

#Extendendo a lista

livrosJohnGreen = ["A culpa é das estrelas", "Quem é voce Alasca?", "Will & Will"]
livrosNicholasSparks.extend(livrosJohnGreen)
print(livrosNicholasSparks)

#Adicionando um item à lista em uma posição especifica

livrosNicholasSparks.insert(0, "A bailarina de Auschwitz")
print(livrosNicholasSparks)

#Removendo item da lista

livrosNicholasSparks.remove("A bailarina de Auschwitz")
print(livrosNicholasSparks)

# Removendo item em uma posição especifica

livrosNicholasSparks.pop(0)
print(livrosNicholasSparks)

#Contando itens na lista

print(livrosNicholasSparks.count("O retorno"))

# Mudando a ordem da lista

# Argumento utilizado para ordenar em ordem alfabética
livrosNicholasSparks.sort()
print(livrosNicholasSparks)

# Invertendo a ordem 'de trás para frente'

livrosNicholasSparks.reverse()
print(livrosNicholasSparks)

# Apagando todos os itens da lista

livrosJohnGreen.clear()
print(livrosNicholasSparks,livrosJohnGreen)