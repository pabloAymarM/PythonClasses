#Dois usuários; Cada um com login e senha:                                                                                                                                 1) A senha não pode ser igual o user;                                                                                                                                       2) O user2 não pode ser igual user1.

user1 = ' '
user2 = ' '
while user1 == ' ':
    user1 = input('Usuário1: ')
    senha1 = input('Senha1: ')
    if(senha1 == user1):
        print('Senha Inválida - REPITA!')
        senha1 = input('Senha1: ')
    else:
        print(f'Seja bem vindo {user1}')
        print('='*20)
while user2 == ' ':
    user2 = input('Usuário2: ')
    senha2 = input('Senha2: ')
    if(senha2 == user2):
        print('Senha Inválida - REPITA!')
        senha2 = input('Senha2: ')
    else:
        print(f'Seja bem vindo {user2}')
  