# 13. Crie um programa que solicite ao usuário três números inteiros. Compute e exiba na tela:
# a) o resto da divisão do primeiro com o segundo;
# b) o segundo exponencial com o terceiro;
# c) o primeiro dividido pelo terceiro, somado com o segundo.


n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceito número inteiro: "))

a = n1 % n2

b = n2 ** n3

c = (n1 / n3) + n2

print("O resto da divisão de", n1, "com", n2, "é", a)

print(n2,"elevado a", n3, "é", b)

print("(", n1, "/", n3, ") +", n2, "=", c)
###