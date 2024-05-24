"""
Faça um jogo que o usuário tenha que acertar a palavra
secreta
- Quando o usuário digitar uma letra, você vai conferir se a letra
digitada está na palavra secreta.
-Se a letra digitada estiver na palavra secreta, exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numeros_tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    numeros_tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numeros_tentativas)
        letras_acertadas = ''
        numeros_tentativas = 0
