# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
import math
print('TRIÂNGULO RETÂNGULO')
co = float(input('Qual o comprimento do cateto oposto:  '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
#hipo = (co ** 2 + ca ** 2 ) ** (1/2)
hipo = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {(hipo)}')