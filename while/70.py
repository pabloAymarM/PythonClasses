#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
ns_conjunto = ('zero', 'um', 'dois', 'três', 'quatro', 'quinta', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    print('Tente novamente!', end=' ')
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o número {ns_conjunto[num]}.')