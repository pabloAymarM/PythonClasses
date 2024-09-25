#Desenvolva uma função chamada calcular_desconto que receba o valor de um produto e o percentual de desconto a ser aplicado, e retorne o valor final com desconto.
#O programa deve solicitar o valor original e a porcentagem de desconto, 
#calcular o preço final e exibir o resultado,
#esse resultado obtido da função deverá ser armazenado em uma lista,
#e no final de tudo essa lista deverá ser exibida com todos os valores.
#o usuário deverá fazer isso 5 vezes.

list = []

def calcDesconto(vlrP, porCen):
    vlrFinal = vlrP - (vlrP * porCen/100)
    
    return vlrFinal

for cont in range(5):
    valor = float(input('Valor original: '))
    desconto = float(input('Desconto: (em %) '))
    list.append(calcDesconto(valor, desconto))

print(list)