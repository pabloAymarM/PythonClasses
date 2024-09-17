#Crie um programa que leia vários números interios pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuara a digitar valores.
res = 'S'
soma = quant =  media = maior = menor = 0
while res in 'Ss':
    n1 = int(input('Digite um número: '))
    soma += n1 
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média é {}.' .format(quant, media))
print('O maior número é {} e o menor {}.' .format(maior, menor))