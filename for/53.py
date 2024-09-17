#Faça um programa que leia o peso de 5 pessoaas. No final, mostre qual foi maior e menor peso lidos.
maior = 0
menor = 0
for people in range(1,6):
    weight = float(input('O peso da {}ª pessoa: ' .format(people)))
    if people == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print('O maior peso lido foi {}Kg.' .format(maior))
print('O menor peso lido foi {}Kg.' .format(menor))    