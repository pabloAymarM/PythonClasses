objetos = ('Lápis', 'Borracha', 'Caderno') #tuple (values immutable)
# objetos = ['Lápis', 'Borracha', 'Caderno'] #list

print(type(objetos))
print(objetos[1])

print('-'*50)

for item in range(0,3):
    print(objetos[item])
    
print('-'*50)

for item in objetos:
    print(item)
    
print('-'*50)

objetos[0] = 'Caneta'
print(objetos)