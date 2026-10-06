def limpar_tela():
    # Código ANSI que limpa a tela e joga o cursor para o topo
    print("\033[H\033[J", end="")
#=====================================
produtos = [
    {'nome': 'arroz', 'preco': 5, 'estoque': 10},
    {'nome': 'feijao', 'preco': 8, 'estoque': 3},
    {'nome': 'macarrao', 'preco': 4, 'estoque': 7}
]
escolha = input('Qual produto deseja vender?: ').lower()
encontrado = False
for produto in produtos:
    if produto['nome'] == escolha:
        encontrado = True
        if produto['estoque'] > 0:
            produto['estoque'] -= 1
            print(f'{produto['nome']} vendido! - {produto['estoque']} no estoque')
            print(f'R${produto['preco']}')
            break
        else:
            print('Fora de estoque!')
            break
if not encontrado:
    print('Produto inexistente!')
    
