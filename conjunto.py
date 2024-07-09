livrosNicholasSparks = {"O desejo", "O retorno", "O melhor de mim","O milagre", "A última música", "A escolha", "Um porto seguro", "Um homem de sorte", "Diario de uma paixão", "Noites de tormenta", "O guardião","O milagre"}

print(livrosNicholasSparks)

# Adicionando item ao conjunto

livrosNicholasSparks.add("Um amor para recordar")
print(livrosNicholasSparks)

# Removendo item do conjunto utilizando o método 'remove' , caso não determine o item que ele deve remover, ele retornará um erro

livrosNicholasSparks.remove("O guardião")
print(livrosNicholasSparks)

# Removendo item do conjunto utilizando o método 'discard', caso não determine um item que contenha no conjunto no qual ele deve remover, ele não fará nada

livrosNicholasSparks.discard("test")
print(livrosNicholasSparks)

# Removendo item do conjunto com o método 'pop', ele irá remover o item que ele quiser, e não definimos qual será

livrosNicholasSparks.pop()
print(livrosNicholasSparks)

# Unindo 2 conjuntos utilizando o método 'union' (de forma aleatória)

livrosJohnGreen = {"A culpa é das estrelas", "Quem é voce Alasca?", "Will & Will","O milagre"}

uniao = livrosNicholasSparks.union(livrosJohnGreen)
print(uniao)

# Retornando o item que contém repetição em 2 conjuntos

intersecao = livrosNicholasSparks.intersection(livrosJohnGreen)
print(intersecao)

# Retornando itens que contém no primeiro conjunto e não contém no segundo conjunto utilizando o método 'difference'

conj1 = {"O milagre", "O guardiao", "Desejo"}
conj2 = { "Desejo", "O milagre", "A ultima musica", "Noites de tormenta"}

diferenca = conj1.difference(conj2)
print(diferenca)

# Retornando um conjunto que contenha valores com diferença simétrica entre os dois conjuntos, ou seja, ele irá comparar os itens de cada conjunto , e retonar os itens que não são iguais entre os dois conjuntos
conj1 = {"O milagre", "O guardiao", "Desejo"}
conj2 = { "Desejo", "O milagre", "A ultima musica", "Noites de tormenta"}

diferenca_simetrica = conj1.symmetric_difference(conj2)
print(diferenca_simetrica)

# Verificando se o segundo conjunto contém o primeiro conjunto dentro (retorna como True ou False) 

conj1 = {"O milagre", "O guardiao", "Desejo"}
conj2 = {"O guardiao", "Desejo", "O milagre", "A ultima musica", "Noites de tormenta"}
conj3 = conj1.issubset(conj2)

print(conj3)

# Verificando se o primeiro conjunto possui todo o segundo conjunto dentro de si

conj1 = {"O milagre", "O guardiao", "Desejo"}
conj2 = {"O guardiao", "Desejo", "O milagre", "A ultima musica", "Noites de tormenta"}
conj3 = conj1.issuperset(conj2)

print(conj3)

# Utilizando o método 'clear' para apagar todos os itens de um conjunto

conj1 = {"O milagre", "O guardiao", "Desejo"}
conj2 = {"O guardiao", "Desejo", "O milagre", "A ultima musica", "Noites de tormenta"}

conj1.clear()

print(conj1, conj2)