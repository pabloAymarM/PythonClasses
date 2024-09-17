#Faça um programa que leia uma frase e mostre:
# - Quantas vezes aparece a letra "a";
# - Em qual posição ela aparece a primeira vez;
# - Em qual posição ela aparece a última vez;

frase = input('Digite uma frase -> ')
frase1 = frase.lower()
print('Tem {} letra(s) "a" nesta frase.' .format(frase1.count('a')))
print('A primeira letra está em: {}' .format(frase1.rfind('a')))
print('A última letra está em {}' .format(frase1.rfind('a')))

