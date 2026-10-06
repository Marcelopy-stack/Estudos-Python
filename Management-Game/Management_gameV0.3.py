def limpar_tela():
    # Código ANSI que limpa a tela e joga o cursor para o topo
    print("\033[H\033[J", end="")
#Globais-Imutáveis=====================================
tabela = [{'nome': 'arroz',
            'estoque': 0,
            'venda': 1.90,
            'compra': 1.50 },
          {'nome': 'feijao',
            'estoque': 0,
            'venda': 2.60,
            'compra': 2.00 },
          {'nome': 'macarrao',
              'estoque': 0,
              'venda': 3.00,
              'compra': 2.30
          }]
#Player================================================
jogador = {'nome': '','empresa': '', 'dinheiro': 50}
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
        for produto in tabela:
            print(f'{produto['nome']}: {produto['estoque']} unidade(s)')
        item = input(('O que você quer vender?: ')).lower()
        for produto in tabela:
            if item == produto['nome']:
                encontrou = True
                if produto['estoque'] > 0:
                    produto['estoque'] -= 1
                    jogador['dinheiro'] += produto['venda']
                    print(f'{produto['nome']} vendido! R${produto['venda']} adicionado ao caixa!')
                else:
                    print('Fora de estoque!')
        if not encontrou:
            print('Produto inexistente')
        d = input('Deseja vender novamente?: ')
        limpar_tela()
def comprar():
    d = 's'
    while d in ('sim', 's'):
        print(f'R${jogador['dinheiro']}')
        print('=' * 20)
        for produto in tabela:
            print(f'Produto: {produto['nome']} - R${produto['compra']} | {produto['estoque']} no seu estoque')
        print('=' * 20)
        compra = input('Qual item deseja comprar?: ').lower()
        for produto in tabela:
            if produto['nome'] == compra:
                encontrado = True
                quantidade = int(input('Quantas unidades desse produto?: '))
                if jogador['dinheiro'] >= produto['compra'] * quantidade:
                    if quantidade > 0:
                        produto['estoque'] += quantidade
                        jogador['dinheiro'] -= produto['compra'] * quantidade
                        print(f'{quantidade} unidades de {produto['nome']} adicionados!')
                    else:
                        print('Nada comprado!')
                        break
                else:
                    print('Dinheiro insuficiente!')
                    break
        if not encontrado:
            print('Item inválido!')
        d = input('Deseja comprar novamente?: ').lower()
        limpar_tela()
def informacoes():
    limpar_tela()
    for informacao in jogador:
        print(f'{informacao}: {jogador[informacao]}')
    print('=' * 20)
    print('Estoque:')
    for chave in tabela:
        print(f'{chave['nome']} - {chave['estoque']} unidade(s) no estoque!')
    print('=' * 20)
    print('Preço de venda:')
    for chave in tabela:
        print(f'{chave['nome']} - R${chave['venda']}')
    print('=' * 20)
    print('Preço de compra:')
    for chave in tabela:
        print(f'{chave['nome']} -  R${chave['compra']}')
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
