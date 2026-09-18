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
        tarefas.append(input('Adicione uma tarefa: '))
        print('Tarefa adicionada!')
#visão de lista
def ver_tarefas():
    for i in range(len(tarefas)):
        print(f'{[i+1]} - {tarefas[i]}')
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
    
