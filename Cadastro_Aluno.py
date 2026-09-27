Aluno = {'nome': '','idade': '', 'série': '', 'notas': ['', '', ''] }
#Menu
def menu():
    print('=' * 20)
    print('1 - Adicionar informações')
    print('2 - Ver informações')
    print('=' * 20)
#Adição de informações
def add_informacao():
    soma = 0
    Aluno['nome'] = input('Digite seu nome: ')
    Aluno['idade'] = int(input('Digite sua idade: '))
    Aluno['série'] = input('Digite sua série: ')
    for i in range(len(Aluno['notas'])):
        Aluno['notas'][i] = float(input('Digite suas nota: '))
        soma += Aluno['notas'][i]
    m = soma / len(Aluno['notas'])
    return m
#Ver informações
def see_informacao():
    for chave in Aluno:
        print(f'{chave}: {Aluno[chave]}')
        
media = add_informacao()
see_informacao()
