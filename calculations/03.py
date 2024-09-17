#Faça um programa que leia um número e mostre na tela seu antecessor e seu sucessor:
n = int(input('Digite um número e descubra seu antecessor e seu sucessor: '))
ant = n - 1
suc = n + 1

print(' O antecessor deste número é: {} e seu sucesssor é: {}' .format(ant,suc))