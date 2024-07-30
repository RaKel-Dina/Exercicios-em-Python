# faça um programa que leia a altura e largura de uma parede em metros, calcule sua área de tinta necessária para
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2M²
alt = float(input('Altura da parede: '))
larg = float(input('Largura da parede: '))
area = alt*larg
tinta = area / 2
print(f'Sua parede tem a dimensão de {alt}x{larg} e sua área é {area}m².')
print(f'Para pintar uma área de {area}m², você vai precisar de {tinta}L de tinta.')