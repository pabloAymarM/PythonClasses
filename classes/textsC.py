#Manipulando Cadeias de Texto
#As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
"""
Cadeia de Caracteres = Frase = String
"""
"""
    Curso em vídeo Pyhton
    01234567891011121314151617181920

    0 - C
    1 - u
    2 - r
    3 - s
    4 - o
    5 - 
    6 - e
    7 - m
    8 - 
    9 - V
    10 - í
    11 - d
    12 - e
    13 - o
    14- 
    15 - P
    16 - y
    17 - t
    18 - h
    19 - o
    20 - n
"""
"""
- Fatiamento:
    frase = 'Curso em vídeo pyhton'
    print (frase[9])
        resultado -> V
    
    print (frase[9:13])
        resultado -> Víde
    
    print (frase[9:21:2])
        -> O '2' diz que a string será lida de dois em dois
        
    print (frase[:5])
        -> Será considerado do início da string, como se fosse: [0:5]; 

    print (frase[15:])
        -> O progrma irá ler do caractere 15 até o final.
    
    print (frase[15::3])
        -> O programa irá de 15 até o final, lendo os caracteres de 3 em 3.
"""
"""
- Análise:
    len(frase)
        -> quantidade de caracteres;
    
    frase.count('o')
        -> O programa irá contar quantos 'o' tem na string;
    
    frase.count('o', 0, 13)
        -> Irá mostrar quantos 'o' aparecem na string do caractere 0 ao 13;
        
    frase.find('deo')
        -> Irá mostar o momento que inicia o 'deo';
        
    frase.find('Android')
        -> Não existe. Ele vai mostrar -1
    
    'Curso' in frase
        -> Irá mostrar 'True' ou 'False'
"""
"""
- Transformação:
    frase.replace('Python','Android')
        -> Irá substituir a palavra 'Python' por 'Android'

    frase.upper()
        -> Irá transformar a string em Maiúsculo
    
    frase.lower()
        -> Irá transformar a string em minúsculo
       
    frase.capitalize()
        -> Irá transformar tudo em minúsculo e a primeira letra ficará em Maiúsculo
    
    frase.title()
        -> Ele fará o capitalize palavra por palavra após um espaço encontrado
        
    fraseN = '   Aprendendo Python  ' 
    fraseN.strip()
        -> Os espaçoes iniciais e finais serão apagados
        
    frase.lstrip()
        -> Os espaços do início serão apagados
    
    frase.rstrip()
        -> Os espaços do final serão apagados
"""
"""
Divisão:
    frase.split()
        -> Cada palavra iá se tornar uma nova string, zerando os caracteres
"""
"""
Junção:
    '-'.join(frase)
        -> Será incluído '-' nos espaços.
"""

frase = 'Curso em Vídeo Python'
print(frase.split()) 