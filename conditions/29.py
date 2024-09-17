#Desenvolva o programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrado R$0,50 por Km para viagens de até 200Km e R$0,45 para viagem mais longas. 
dis = float(input('Distância da viagem em KM: '))
if dis <= 200:
    print('Sua viagem custará R${:.2f}' .format(dis*0.5))
else: 
    print('Sua viagem custará R${:.2f}' .format(dis*0.45))