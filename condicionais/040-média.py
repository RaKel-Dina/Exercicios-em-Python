# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
nota = (n1 + n2)/2

if nota < 5:
    print(f'REPROVADO | Média [{nota}] \nEstá abaixo da média.')
elif nota >= 7:
    print(f'APROVADO | Média [{nota}]')
else:
    print(f'RECUPERAÇÃO | Média [{nota}]\nO aluno precisa de {7 - nota} pontos para ser aprovado.')
