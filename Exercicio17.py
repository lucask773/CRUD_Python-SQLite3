while True:
    lista = []
    print(lista)
    comeco = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ')
    
    if 'i' in comeco:
        produto = input('Insira um produto:')
        lista.append(produto)
    
    if 'a' in comeco:
        indice = int(input('Escreva o índice do produto que quer apagar:'))
        if 0 <= indice < len(lista):
            del lista[indice]
            print(f'O produto no índice {indice} foi removido.')
        else:
            print(f'O índice {indice} está fora dos limites da lista.')

    if 'l' in comeco:
        for indice, nome in enumerate(lista):
            print(indice, nome)

