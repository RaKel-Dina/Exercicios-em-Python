# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
# sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Em que ano você nasceu: '))
ano = date.today().year
idade = ano - nascimento
if idade > 18:
    print(f"Você tem {idade} anos de idade, já passou {idade-18} ano(s) do alistamento.")
elif idade < 18:
    print(f'Você tem {idade} anos de idade, ainda faltam {18-idade} ano(s) para o alistamento.')
else:
    print(f'Você tem {idade} anos de idade, está na idade exata para se alistar. ')
