viagem = float(input('Qual a distancia da viagem: '))
print(f'Vocẽ está prestes a fazer uma viagem de {viagem:.2f}Km.')
preco = viagem * 0.50 if viagem <=200 else viagem * 0.45
print(f'O custo da sua viagem ficará em R${preco} ')

