# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugou o carro? '))
km = float(input(f'Quantos Km rodou? '))
valor_dia = 60 * dias
valor_km = 0.15* km
total = valor_dia + valor_km
print(f'Total de {dias} dias ficará em = R${valor_dia}, total de {km}Km = R${valor_km}')
print(f'Total a pagar = R${total}.')

