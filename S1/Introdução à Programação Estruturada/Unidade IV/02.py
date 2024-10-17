# 2.
# Crie um programa que leia uma lista com cinco notas, calcule a média e mostre na tela.

lista = []

for i in range(5):
    nota = float(input(f"Digite nota {i+1}: "))
    lista.append(nota)

media = sum(lista) / len(lista)

print("A média das notas é ", media)