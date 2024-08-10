#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
casa = float(input('Qual é o valor da casa: '))
salario = float(input('Quanto é o salário: '))
vezes = float(input('Em quantos anos vai pagar: ')) * 12
mensalidade = (casa/vezes)
porc = (mensalidade/salario)*100
if porc <= 30:
    print(f'PARABÉNS! Seu empréstimo bancário foi aprovado!')
    print(f'Você pagará R${mensalidade:.2f} por mês, por {int(vezes/12)} anos')
elif porc > 30:
    print(f'REPROVADO: As prestações mensais no valor de R${mensalidade:.2f} excederão 30% do seu salário.')



