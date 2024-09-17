#Esccreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salárioos superiores a R$1.245,00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite seu salário: R$'))
if sal > 1245.00:
    cal = sal * 0.15
    print('Seu salário atual será de R${:.2f}' .format(sal + cal))
else:
    cal1 = sal * 0.10
    print('Seu salário atual será de R${:.2f}' .format(sal + cal1))