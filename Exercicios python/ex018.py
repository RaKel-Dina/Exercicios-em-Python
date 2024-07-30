#aça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Qual o valor do ângulo: '))

s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))

print(f'Para o ângulo de {angulo}º:', f'\nO seno é {s:.2f}.', f'\nO cosseno é {c:.2f}.', f'\nE a tangente é {t:.2f}.')