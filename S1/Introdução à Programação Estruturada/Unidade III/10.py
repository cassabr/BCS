# 10. 
# Faça um programa que receba uma matriz 3x3 e multiplique-a pelo escalar 5. 
# Mostre o resultado na tela.

import numpy as np

print("Matriz")

matriz = \
    np.array([input("0,0: "), input("0,1: "), input("0,2: "),
             [input("1,0: "), input("1,1: "), input("1,2: ")]])

print(matriz*5)
