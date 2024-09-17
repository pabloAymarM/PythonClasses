nome1 = str(input("Crie um usuário: \n"))
senha1 = str(input("Crie uma senha: \n"))
    
nome2 = str(input("Confirme o seu nome de usuário: \n"))
senha2 = str(input("Confirme sua senha: \n"))
    
if nome1 != nome2:
    print("Usuário inválido!")
if nome1 == nome2:
    print("Usuário válido")
if senha1 != senha2:
    print("Senha incorreta!\n")
else:
    print("Senha Confirmada!\n")