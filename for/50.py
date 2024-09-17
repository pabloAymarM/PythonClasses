#Faça um programa que leia um núemro inteiro e diga se ele é ou não um núemro primo.
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.' .format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')