#some uma lista a outra. No final, armazene o resultado em outra lista.

numList = 0
list1 = []
num1 = 1
list2 = []
num2 = 1

while num2 != 0:
    num1 = int(input('Informe n1 (Digite 0 para parar): '))
    list1.append(num1)
    num2 = int(input('Informe n2 (Digite 0 para parar): '))
    list2.append(num2)
    
list3 = []

for elemento in list1:
    list3.append(list1[numList] + list2[numList])
    numList += 1

list3.pop()
print(list3)
