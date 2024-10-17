# 9. 
# Faça um programa que receba duas matrizes 2x2 pelo usuário e some-as. 
# Mostre o resultado na tela. Dica: Use o NumPy.

import numpy as np

print("Matris 1")

matriz_1 = np.array([input("0,0: "), input("0,1: "),
    [input("1,0: "), input("1,1: ")]])

print("Matris 2")
matriz_2 = np.array([input("0,0: "), input("0,1: "),
    [input("1,0: "), input("1,1: ")]])

print(matriz_1 + matriz_2)