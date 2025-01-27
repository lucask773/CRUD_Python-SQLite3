primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

if primeiro_valor >= segundo_valor:
    print('{} é maior que {}'.format(primeiro_valor,segundo_valor))

elif segundo_valor >= primeiro_valor:
    print('{} é maior que {}'.format(segundo_valor,primeiro_valor))

elif primeiro_valor == segundo_valor:
    print('{} são iguais {}'.format(primeiro_valor,segundo_valor))

else:
    print('Você não digitou nada.')
