#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Informe o valor do produto: R$ '))
desconto = (valor*5)/100
print(f'O produto custa {valor} com 5% de desconto passará a custar R$ {valor - desconto}.')