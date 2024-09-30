#Crie uma função chamada comparar_idades que receba duas idades e retorne qual das duas é maior. O programa deve solicitar as idades de duas pessoas e usar a função para exibir qual delas é mais velha, ou se têm a mesma idade. O usuário deverá fazer isso enquanto desejar, ou até digitar o número zero

esc = 1

def compararIdades(idd1, idd2):
        if idd1 > idd2:
            print(f'A idade {idd1} é maior que {idd2}.')
        elif idd2 > idd1:
            print(f'A idade {idd2} é maior que {idd1}.')
        elif idd1 == idd2:
            print('As idades são iguais.')

while esc != 0:       
    i1 = int(input('Informe a primeira idade: '))
    i2 = int(input('Informe a segunda idade: '))        
    compararIdades(i1,i2)
    esc = int(input('Deseja continuar? ([0.NÃO] [1.SIM]) '))