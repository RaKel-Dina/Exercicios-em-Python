#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
# aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Quanto está o seu salário: '))
if salario > 1250:
    novo_salario = salario + ((salario * 10)/100)
    print(f'Seu novo salário terá um aumento de 10%. Você receberá R${novo_salario:.2f}. ')
if salario <= 1250:
    novo_salario = salario + ((salario * 15)/100)
    print(f'Seu novo salário terá um aumento de 15%. Você receberá R${novo_salario:.2f}. ')

print()