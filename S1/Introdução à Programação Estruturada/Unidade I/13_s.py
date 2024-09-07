# 13. Crie um programa que solicite ao usuário três números inteiros. Compute e exiba na tela:
# a) o resto da divisão do primeiro com o segundo;
# b) o segundo exponencial com o terceiro;
# c) o primeiro dividido pelo terceiro, somado com o segundo.


a = input("Digite um numero 1: ")
b = input("Digite um numero 2: ")
c = input("Digite um numero 3: ")

print("Resto da divisão do primeiro com segundo: " + str(a%b))

print("Primeiro dividido pelo terceiro somado com o segundo: " + str(b**c))

print("Primeiro dividido pelo terceiro somado com o segundo: " + str((a/c)+b))