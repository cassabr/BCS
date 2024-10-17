# 3. 
# Crie um programa que leia uma lista de seis números inteiros e imprima-os na ordem inversa da leitura.

lista = []

for i in range(6):
    numeros = int(input(f"Digite o {i+1} número: "))
    lista.append(numeros)

print(lista[::-1])