# 7. 
# Utilizando conjuntos (set) em Python, crie um programa que receba 10 números 
# e imprima cada um deles, mas, caso tenha algum repetido, deve ser impresso somente uma vez.

conjunto = set()

for i in range(10):
    conjunto.add(input(f"igite o número {i+1}: "))
print(conjunto)