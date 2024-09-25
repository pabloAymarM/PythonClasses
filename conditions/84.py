#Bônus de salário
sal = float(input('Informe o seu salário: '))
anos = int(input('Há quantos anos você trabalha na empresa? '))

if anos <= 5:
    sal *= 1.05
    print(f'Você ganhou um bônus de 5% e seu novo salário é R${sal}')
elif anos > 5 and anos <= 10:
    sal *= 1.1
    print(f'Você ganhou um bônus de 10% e seu novo salário é R${sal}')
elif anos > 10:
    sal *= 1.15
    print(f'Você ganhou um bônus de 15% e seu novo salário é R${sal}')