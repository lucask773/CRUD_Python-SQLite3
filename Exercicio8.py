"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Escreva seu nome:')

tamanho_nome = len(nome) 

if tamanho_nome > 1:

    if tamanho_nome <= 4:
        print('Seu nome é pequeno')
    if tamanho_nome <= 5 or tamanho_nome <= 6:
        print('Seu nome é mediano')
    if tamanho_nome >= 7:
        print('Seu nome é grande')
else:
    print('digite algo')