senha = 'amor'
senha_invisivel = '****'
digitado = ''
repetidos = 0

while True: 
    if digitado != senha:
        digitado = input(f'Escreva novamente({repetidos}x): ')
        repetidos += 1
    if len(digitado) > 1:
        print('Digite apenas uma letra.')
        continue

    if 'a' in digitado:
        senha_invisivel = senha_invisivel[:0] + 'a' + senha_invisivel[0:]
        print(senha_invisivel)
    if 'm' in digitado:
        senha_invisivel = senha_invisivel[:1] + 'm' + senha_invisivel[1:]
        print(senha_invisivel)
    if 'o' in digitado:
        senha_invisivel = senha_invisivel[:2] + 'o' + senha_invisivel[2:]
        print(senha_invisivel)
    if 'r' in digitado:
        senha_invisivel = senha_invisivel[:3] + 'r' + senha_invisivel[3:]
        print(senha_invisivel)

    if 'amor' in senha_invisivel:
        print(f'Parabens!, a senha é {senha_invisivel}')
        break


#JEITO CERTO
    
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0