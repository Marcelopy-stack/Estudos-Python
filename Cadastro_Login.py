import random
#Banco de senhas/nome
senha_forte = ('2gdj@#Dhs','3djwo%hs#','*hsha@#!shu','fjwdb@3ej@')
nome = input('Digite seu nome: ')
#Email
def email():
    d = 'n'
    while d in ('n','nao', 'não'):
        address = input('Adicione um endereço de email: ')
        d = input(f'{address} está correto (s/n)?' ).lower()
    return address
#Senha
def senha():
    d = 'n'
    while d in ('n','nao', 'não'):
        d_s = input('Deseja gerar uma senha extra forte? (s/n) ').lower()
        if d_s == 's' or d_s == 'sim':
            password = random.choice(senha_forte)
            break
        else:
            password = input('Adicione uma senha forte: ')
        d = input(f'{password} está correto (s/n)? ' )
    return password
#Cadastro
def cadastro(address, password):
    d = 's'
    while d in ('s','sim',):
        v_address = input('Coloque seu email: ')
        v_password = input('Coloque sua senha: ')
        if address == v_address and v_password == password:
            print(f'Tudo correto, seja bem vindo! {nome}')
            break
        else:
            d = input(' deseja tentar novamente? (s/n): ').lower()



address = email()
password = senha()
cadastro(address, password)
