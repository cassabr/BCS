# 6. 
# Faça um programa que receba um nome de arquivo e que leia esse arquivo linha a linha e imprima-o na tela.

arquivo = open("E:\Sabrina Arquivos Pessoais\gemini.txt", "r")

for linha in arquivo:
    print(linha)
arquivo.close()