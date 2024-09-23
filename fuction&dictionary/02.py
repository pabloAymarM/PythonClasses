#crie uma função chamada 'addTemperatura' 
#armazene e solicite 5 temperaturas
#e armazena em um dicionário 
#e exiba o dicionário

temp = ' '
cont = 0
tempDic = {
    
}

def addTemperatura(temp1):
        resultado = tempDic[f'Temp: {cont - 1}'] = temp1
        
        return resultado 

for cont in range(1, 6):
    temp = float(input(f'Infome a temperatura {cont}: '))
    cont += 1
    
    addTemperatura(temp)
    
print(tempDic)