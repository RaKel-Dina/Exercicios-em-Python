# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece  a letra "A"
# Em que posição posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip().upper()
print(f"A letra 'A' aparece {frase.count('A')} vezes.")
print(f"Ela aparece primeiro na posição {frase.find('A')}")
print(f"Aparece na por ultimo na posição: {frase.rfind('A')}")
