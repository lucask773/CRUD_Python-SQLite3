"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome:
    pass
else: 
    print('Desculpe, você não digitou nada')
if idade:
    pass
else:
    print('Desculpe, você não digitou nada')


nome_invertido = (nome[::-1])
numero = len(nome)
primeira = (nome[0])
ultima = (nome[-1])
print(f'Seu nome é {nome}')
print('Seu nome invertido é {}'.format(nome_invertido))
print(f'Seu nome tem {numero} letras')
print(f'A primeira letra do seu nome é {primeira}')
print(f'A ultima letra do seu nome é {ultima}')



if ' ' in nome:
    print('Seu nome possui espaço')
elif nome not in ' ': 
    print('Seu nome não possui espaços')    

