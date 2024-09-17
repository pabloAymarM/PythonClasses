#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar;
# Se é a hora de se alistar;
# Se já passoudo tempo de alistamento;

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo:

nasc = int(input('Data de nascimento: '))
idade = 2023 - nasc

if idade < 18:
    tempo = 18 - idade
    print('Você tem {} e falta {} anos para você se alistar.' .format(idade, tempo))
    print('Você ainda vai se alistar no exército.')
elif idade == 18:
    print('Está na hora de você se alistar no exército.')
elif idade > 18:
    tempo = idade - 18
    print('Você tem {} e já passou {} anos do seu alistamento.' .format(idade, tempo))
    print('Já passou o tempo de alistamento no exército.')
