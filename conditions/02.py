while True:
    word1 = str(input("Digite sua senha: \n"))
    word2 = str(input("Confirme sua senha: \n"))
    if word1 != word2:
        print("Chave incorreta!\n")
    else:
        break
    print("Chave válida!")