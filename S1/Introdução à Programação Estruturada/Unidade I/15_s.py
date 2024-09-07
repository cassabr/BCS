# 15. 
# Construa um programa que receba o tamanho dos catetos de um triângulo retângulo e compute sua hipotenusa. 
# Imprima o valor da hipotenusa na tela.

import math

c1 = int(input("Digite o cateto 1: "))

c2 = int(input("Digite o cateto 2: "))

h = math.sqrt(c1**2 + c2**2)

print("O valor da hipotenusa é: ", h)