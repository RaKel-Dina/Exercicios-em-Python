# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
#entrada de dados
num_usuario = int(input('Adivinha qual número vou escolher entre 1 e 5: '))

# processamento de dados
n = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
print()
print(30*'==')
if num_usuario == n:
    print(f"Eu pensei no número {n}, você digitou o número {num_usuario}, Parabéns, você ganhou!!!")
else:
    print(f'Eu pensei no número {n}, você digitou o número {num_usuario}, você perdeu.')
print(30*'==')
print()