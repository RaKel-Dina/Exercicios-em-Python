#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print(f'{num} é número par.')
else:
    print(f'{num} é número ímpar.')