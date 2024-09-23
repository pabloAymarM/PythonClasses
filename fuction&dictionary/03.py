#crie um dicionário 'poucos produtos'
#guarde o preço de 4 produtos
#solicite o nome do produto (exiba o preço) 
#se não estiver no dicionário: print('Produto não encontrado.')  

dicProd = {
    'Vestido' : 250.0,
    'Sapato' : 300.0,
    'Tênis' : 200.0,
    'Óculos' : 90.0
}

prod = str(input('Pesquise o produto: '))

if prod in dicProd.keys():
    print('ok')