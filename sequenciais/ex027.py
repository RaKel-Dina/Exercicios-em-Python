# Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida o primeiro e o último
# nome sepadaramente.
nome_completo = str(input('Digite seu nome completo: ')).strip()
print(nome_completo)
nome_completo = nome_completo.split()
print(f'Primeiro nome: {nome_completo[0]}')
print(f'Último nome: {nome_completo[-1]}')
