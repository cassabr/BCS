# 16. 
# Crie um programa que recebe como entrada dois números inteiros, 
# divida o primeiro número pelo segundo e imprima na tela, separadamente, a parte inteira da divisão e o resto.

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

div = n1 / n2

p_mod = div - int(div)

print("A divisão resulta em ",div,", ou seja, ", int(div), "mais", p_mod)