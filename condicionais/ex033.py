#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# processamento de dados
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'{maior} é o número maior.')
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'{menor} é o número menor.')