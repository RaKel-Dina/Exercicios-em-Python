# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO"
cidade = str(input('Qual o nome da cidade: ')).strip().upper()
cidade = cidade.split()
print('SANTO' in cidade[0])