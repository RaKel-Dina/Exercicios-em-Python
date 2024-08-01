#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do
# limite.

velocidade = float(input('Velocidade do carro: '))
if velocidade <= 80.0:
    print(f'VELOCIDADE: {velocidade}km. O carro está dentro do limite de velocidade, não há multas.')
else:
    km = velocidade - 80.0
    multa = 7.0 * km
    print(f'VELOCIDADE: {velocidade}km. O carro ultrapassou {km}km do limite de velocidade. R${multa:.2f} de multa.')