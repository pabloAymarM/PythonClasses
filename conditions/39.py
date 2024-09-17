#A confederação de natação precisa de um programa que leia a data de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9: Mirim
# até 14: Infantil
# até 19: Júnior
# até 20: Sêmior
# acima: Master

nasc = int(input('Data de nascimento: '))
idade = 2023 - nasc

if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Júnior')
elif 19 < idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')
print('O atleta tem {} anos.'.format(idade))