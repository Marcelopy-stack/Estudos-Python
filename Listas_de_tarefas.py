tarefas = ['oi','ola']
#Menu
def menu():
    print('='*20)
    print('1 - Adicionar item ')
    print('2 - Ver lista ')
    print('3 - Remover item')
    print('='*20)
#Adição de tarefas
def add_tarefas():
        tarefas.append(input('Adicione uma tarefa: '))
        print('Tarefa adicionada!')
#visão de lista
def ver_tarefas():
    for i in range(len(tarefas)):
        print(f'{[i+1]} - {tarefas[i]}')
    
    
ver_tarefas()
