listProdutos = {
    'celular':'R$ 1.500,00',
    'camera': 'RS 1.000,00',
    'fone de ouvido': 'R$ 800,00',
    'monitor': 'R$ 2.000,00'
}


def adicionaProduto(listProdutos):
    produto = input('Digite novamente o nome do produto: ')

    if produto in listProdutos:
        print(f'O valor do produto é: {listProdutos[produto]}')
    else:
        print('Produto não cadastrado, deseja cadastrar?')
        resposta = input('Digite sim ou não: ').lower()
        if resposta == 'sim':
            produto = input('Digite o nome do produto:')
            valor = float(input('Digite o valor do produto: '))
            # listProdutos.update({produto: valor})
            listProdutos[produto] = f'R${valor}'
            print('Produto cadatrado com sucesso!')
            print(f'{listProdutos}')
        elif resposta == 'não':
            print('Ok, volte sempre!')


def consultaList (listProdutos):

    produto = input('Digite o nome do produto:')
    if produto in listProdutos:
        print(f'O valor do produto é: {listProdutos[produto]} ')
    elif produto not in listProdutos:
        adicionaProduto(listProdutos)
        

consultaList(listProdutos)