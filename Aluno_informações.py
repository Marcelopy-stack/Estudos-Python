aluno = {'Nome': '', 'Idade': '', 'Curso': '', 'Nota': ''}
def add_informacoes():
    aluno['Nome'] = input('Digite seu nome: ')
    aluno['Idade'] = int(input('Digite sua idade: '))
    aluno['Curso'] = input('Digite seu curso: ')
    aluno['Nota'] = float(input('Digite sua nota: '))
def ver_informacoes():
    for i in aluno:
        print(f'{i}: {aluno[i]}')
        
add_informacoes()
ver_informacoes()

