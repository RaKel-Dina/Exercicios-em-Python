#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#num = int(input('Digite um número para a conversão: '))
base = int(input(f"CONVERSOR DE BASES NUMÉRICAS \n[1] {5*'_'} Binário \n[2] {5*'_'} Octal \n[3] {5*'_'} Hexadecimal \nOPÇÃO: "))
num = int(input('Escolha um número em decimal: : '))
if base == 1:
    print(f'{num} em binário é: {bin(num)[2:]}')
elif base == 2:
    print(f'{num} em octal: é: {oct(num)[2:]}')
elif base == 3:
    print(f'{num} em hexadecinal é: {hex(num)[2:]}')
