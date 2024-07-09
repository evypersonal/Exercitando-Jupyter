# Exemplo de criação de dicionario

livrosNicholasSparks = {
    "Nome": "O desejo",
    "Autor": "Nicholas Sparks",
    "Ano": 2004,
    "Genero": "Romance",
    "Editora": "Editora Record"
}

print(livrosNicholasSparks)

# Adicionando um item ao dicionário (utilizando o update)

livrosNicholasSparks.update({"classificacao" : 4})
print(livrosNicholasSparks)

# Adicionando um item ao dicionario (utilizando o setdefault)

comentario = livrosNicholasSparks.setdefault("Comentário", "Muito Bom")
print(comentario)

# Atualizando valores ao dicionario

livrosNicholasSparks["Editora"] = "intríseca"
print(livrosNicholasSparks)

# Imprimindo as chaves seguindo com seus valores
itens = livrosNicholasSparks.items()
print(itens)

# Imprimindo todas as chaves do dicionario

chaves = livrosNicholasSparks.keys()
print(chaves)

# Imprimindo todos os valores do dicionario

valores = livrosNicholasSparks.values()
print(valores)

# Removendo um item do dicionario

livrosNicholasSparks.pop("Nome")
print(livrosNicholasSparks)

# Acessando um valor existente (método GET) Caso não exista o valor ele retornará NONE

nome = livrosNicholasSparks.get("Nome")
autor = livrosNicholasSparks.get("Autor")
print(nome, autor)

# Utilizando popitem para remover o último item do dicionario

livrosNicholasSparks.popitem()
print(livrosNicholasSparks)

# Consultando o valor de uma chave utilizando "setdefault"

opcao = livrosNicholasSparks.setdefault("Genero")
print(opcao)

# Apagando todos os itens do dicionario

livrosNicholasSparks.clear()
print(livrosNicholasSparks)

# Utilizando o método fromkeys para criar um novo dicionario




