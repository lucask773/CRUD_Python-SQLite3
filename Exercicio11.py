while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    operador_1 = num_1_float + num_2_float



    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        pass
    else:
        print('Você não digitou um numero valido')

     if '+' in operador:
         print(f'A soma é {operador_1}') 

    


    






    sair = input('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break