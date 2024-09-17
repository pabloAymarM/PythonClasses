#Informe números até que o usuário digite 0. Quando parar, informe quantos são ímpares.
numbers = 1
numImp = 0
while numbers != 0:
    numbers = int(input('Informe números (Se quiser parar, digite 0): '))
    if numbers % 2 != 0:
        numImp += 1  
print(f'Números Ímpares: {numImp}')