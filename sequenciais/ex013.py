#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal_antigo = float(input('Salário atual: '))
aumento = sal_antigo + (sal_antigo * 15 / 100)
print(f'O salário antigo era R${sal_antigo}, com 15% de aumento passará a ser R$ {aumento:.2f}. ')