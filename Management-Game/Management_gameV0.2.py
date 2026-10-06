def limpar_tela():
    # Código ANSI que limpa a tela e joga o cursor para o topo
    print("\033[H\033[J", end="")
#Globais-Imutáveis=====================================
preco_venda = {'arroz': 1.90, 'feijao': 2.60, 'macarrao': 3.00}
preco_compra = {'arroz': 1.50, 'feijao': 2.00, 'macarrao': 2.30}
#Player================================================
jogador = {'nome': '','empresa': '', 'dinheiro': 0}
estoque = {'arroz': 1, 'feijao': 1, 'macarrao': 1}
jogador['nome'] = input('Digite seu nome: ')
jogador['empresa'] = input('Digite o nome da sua empresa: ')
limpar_tela()
#Funções===============================================
def menu(titulo):
    print(f'{titulo} | R${jogador['dinheiro']}')
    print('=' * 20)
    print('1 - Vender')
    print('2 - Comprar')
    print('3 - Ver informações')
    print('4 - Sair')
    print('=' * 20)
    escolha = input('O que você quer acessar?: ').lower()
    limpar_tela()
    return escolha
def vender():
    d = 's'
    while d in ('sim', 's'):
        for produto in estoque:
            print(f'{produto}: {estoque[produto]} unidade(s)')
        produto = input(('O que você quer vender?: ')).lower()
        if produto in estoque:
            if estoque[produto] > 0:
                estoque[produto] -= 1
                jogador['dinheiro'] += preco_venda[produto]
                print(f'{produto} vendido! R${preco_venda[produto]} adicionado ao caixa!')
            else:
                print('Fora de estoque!')
        else:
            print('Produto Inexistente')
        d = input('Deseja vender novamente?: ')
        limpar_tela()
def comprar():
    d = 's'
    while d in ('sim', 's'):
        print(f'R${jogador['dinheiro']}')
        for produto in estoque:
            print(f'Produto: {produto} - R${preco_compra[produto]} |{estoque[produto]} no estoque')
        compra = input('Qual item deseja comprar?: ').lower()
        if compra in estoque:
            quantidade = int(input('Quantas unidades desse produto?: '))
            if jogador['dinheiro'] >= preco_compra[compra]:
                if quantidade > 0:
                    estoque[compra] += quantidade
                    jogador['dinheiro'] -= preco_compra[compra] * quantidade
                    print(f'{quantidade} unidades de {compra} adicionados!')
                else:
                    break
            else:
                print('Dinheiro insuficiente!')
        else:
            print('Item inválido!')
            break
        d = input('Deseja comprar novamente?: ').lower()
    limpar_tela()
def informacoes():
    limpar_tela()
    for informacao in jogador:
        print(f'{informacao}: {jogador[informacao]}')
    print('===============')
    print('No estoque')
    for produto in estoque:
        print(f'{produto}: {estoque[produto]}')
    print('===============')
    print('Preço de venda')
    for precoV in preco_venda:
        print(f'{precoV}: R${preco_venda[precoV]}')
    print('===============')
    print('Preço de compra')
    for precoC in preco_compra:
        print(f'{precoC}: R${preco_compra[precoC]}')
def saida():
    sair = input('Deseja sair?: ')
    return sair
#Código-Rodando========================================
sair = 'nao'
while sair in ('nao', 'n', 'não'):
    escolha = menu(jogador['empresa'])
    if escolha in ('1', 'vender', 'venda'):
        vender()
    elif escolha in ('2', 'comprar', 'compra'):
        comprar()
    elif escolha in ('3', 'ver informações', 'informações'):
        informacoes()
    elif escolha in ('4', 'sair'):
        sair = saida()
