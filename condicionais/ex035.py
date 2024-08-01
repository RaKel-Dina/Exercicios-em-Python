#Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.
r1 = float(input('primeira reta:'))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if (r1 + r2) > r3:
    print('Pode formar triangulo.')
else:
    print('Não pode formar triângulo.')
print()
