# 4. 
# Construa um programa que receba do usuário uma lista com oito números inteiros, calcule e imprima a soma dos quadrados desses números.

lista = []
quadrados = 0

for i in range(8):
    numeros = int(input(f"Digite o {i+1} número: "))
    lista.append(numeros)

for n in lista:
    quadrados += n**2

print(quadrados)