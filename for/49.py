#Desenolva um programa que leia primeiro termo de uma PA. No final, mostre os 10 primeiros termos dessa progresso.
pr = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
décimo = pr + (10 -1) * rz
print('='*30)
for c in range(pr, décimo, rz):
    print('{}'.format(c), end=' ¬ ')
print('ACABOU')