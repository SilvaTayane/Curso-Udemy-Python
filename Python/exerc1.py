# Flag (Bandeira) - Marcar um local
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade

# Algoritmo = Uma solução criada para determinado problema

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        impar_texto = 'par'
    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
