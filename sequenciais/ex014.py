#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
celsius = float(input('Quantos graus estão fazendo? '))
fahrenheit = celsius * 9 /5 + 32
print(f"{celsius}ºC convertidos em Fahrenheit são {fahrenheit}ºF.")