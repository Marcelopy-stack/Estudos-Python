dicionario = {}
tarefas = []
#Menu
def menu():
    print('='*20)
    print('1 - Adicionar item ')
    print('2 - Ver lista ')
    print('3 - Remover item')
    print('='*20)
    selecao = input('Selecione uma opção: ').lower()
    return selecao
#Adição de tarefas
def add_tarefas():
    dicionario['nome'] = input('Digite o nome de sua tarefa: ')
    dicionario['urgencia'] = input('Digite a urgência: ')
    tarefas.append(dicionario)
    print('Tarefa adicionada')
#visão de lista
def ver_tarefas():
    for tarefa in tarefas:
        print(f'[ ] {tarefa['nome']} - {tarefa['urgencia']}')
        print()
#Deletar itens
def remove_tarefas():
    tarefas.remove(input('Remova uma tarefa da lista: '))
    print('Tarefa removida!')

d = 's'
while d in ('s','sim'):
    select = menu()
    if select == '1' or select == 'adicionar item':
        add_tarefas()
    elif select == '2' or select == 'ver lista':
        ver_tarefas()
    elif select == '3' or select == 'remover item':
        remove_tarefas()
    else:
        print('Inválido!')
    d = input('Deseja repetir? (s/n): ')
    
