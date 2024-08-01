# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens
# mais longas.

viagem = float(input('Qual a distancia da viagem: '))
if viagem <= 200:
    valor_normal = viagem * 0.50
    print(f'Uma viajem de {viagem}km custará R${valor_normal:.2f}.')
else:
    valor_longo = viagem * 0.45
    print(f'Uma viajem mais longa de {viagem}km custará R${valor_longo:.2f}')

