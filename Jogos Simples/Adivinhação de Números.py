#minigame pra adivinhar numeros de 1 à 10
from time import sleep
from random import randint


cont = 'S'
resp = 'S'
print('=' * 25)
print('  **JOGO DOS NÚMEROS**')
print('Estou pensando em um número...')
print('   Está entre 1 e 5...')
print('   Consegue adivinhar?')
print('=' * 25)
while cont == resp:
    sleep(2)
    numPc = randint(1, 5)
    print('PENSANDO...')
    sleep(2)
    palp = int(input('PRONTO... dê o seu palpite: '))
    if palp == numPc:
        print('PARABÉS, VOCE ACERTOOOOOOU!!!!!')
        print('`*&`*&`*&`**`*&`*&``&`*&`*&`*&`**&`*&')
    else:
        print('O número certo era ', numPc)
        print('Não foi dessa vez... :/')
    print('=' * 25)
    resp = input('Quer continuar? S/N: ').upper()
