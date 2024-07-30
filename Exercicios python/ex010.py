# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$ 1 = R$ 3,27
dinheiro = float(input('Quanto você tem na carteira? R$ '))
dolar = dinheiro/ 3.27
print(f'Com R${dinheiro} você pode comprar US${dolar:.2f}.')