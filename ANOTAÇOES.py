# = comentarios

print() = fazer aparecer no classmethod

""" """ = docstring,  o python lê

"sep=''" = separador coloca algo para separar 

"\r e \n"= quebra linha

"end=''"= adiciona algo no final do indicado

TIPOS DE DADOS:

"\" = escape, ignora um caractere

int = numero inteiro

float = numero flutuante Ex= 1.1, 10.12, 2
 
type() = diz qual o tipo

boolean = verdeiro ou falso

"==" = é igual?


VARIAVEIS

nome_variavel = expressão

Ex: 
nome_completo = Kevin Lucas
print(nome_completo)

soma = 2 + 2

OPERADORES ARITIMETICOS

adiçao = 10+10

subtraçao = 10-5

multiplicaçao = 10 * 10

divisao = 10/2.2


divisao_inteira = 10 // 2.2

exponenciaçao = 2 ** 10

modulo, resto da divisao = 55 % 2

CONCATENAÇÃO E REPETIÇÃO

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

F-STRINGS

f= permite colocar variaveis no meio do print

:.2f = limitar a 2 casas decimais

.format() = jeito de formatar strings

input = fazer usuario escrever algo

if = se 

elif = se não se

else = se não 

"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

and

or

not

in

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
    
""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')










"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""



id = nome de algo na memória

Ex:

v1 = 'a'

print(id(v1))

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""


Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
 

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

