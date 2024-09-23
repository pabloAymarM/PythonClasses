#Crie um programa que pergunte ao usuário qual foi a velocidade registrada de um veículo e o limite de velocidade da via. Se o veículo estiver acima do limite, o programa deve calcular e exibir o valor da multa, conforme as seguintes regras:                             Até 10 km/h acima do limite: R$ 50,00.                                                                                               Entre 11 e 20 km/h acima do limite: R$ 100,00.                                                                                        Mais de 20 km/h acima do limite: R$ 200,00.                                                                                             Se o veículo estiver dentro do limite, exiba "Sem multa".

velRegistrada = float(input('Informe a velocidade do veículo: ')) 
velLimite = float(input('Informe o limite da via: '))

if velRegistrada >= velLimite + 10:
    multa = 50
    print(f'Sua multa é R${multa}')
elif velRegistrada >= velLimite + 11 and velRegistrada <= velLimite + 20:
    multa = 100
    print(f'Sua multa é R${multa}')
elif velRegistrada > velLimite + 20:
    multa = 200
    print(f'Sua multa é R${multa}')
else:
    print('Sem Multa.')
