# Faça um programa que leia algo pelo teclado e moste na tela o seu tipo primitivo e toda as informações possíveis
# sobre ele.
var = input('Digite algo: ')
print(f"O tipo primitivo desse valor é: {type(var)} ")
print(f'Só tem espaços: {var.isspace()}')
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f"É alfanumérico: {var.isalnum()}")
print(f'Está em letras maiúsculas? {var.isupper()}')
print(f'Está em letras minúsculas? {var.islower()}')
print(f'Está capitalizada? {var.istitle()}')