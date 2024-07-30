#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas.
# o nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar os espaços
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
total_espacos = nome.count(' ')
total_letras = len(nome)
print(f'Total de letras no nome: {total_letras - total_espacos}')
nome = nome.split()
print(f'Total de letras do primeiro nome: {len(nome[0])}')

