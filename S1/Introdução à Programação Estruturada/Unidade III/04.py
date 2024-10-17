# 4. 
# Crie um programa que receba uma string com uma frase digitada pelo usuário. 
# Conte quantos espaços em branco existem na string e quantas vezes aparecem cada uma das vogais A, E, I, O e U.

frase = input("Digite uma frase: ")
print("Espaços: " + str(frase.count(" ")))
print("a: " + str(frase.count("a")))
print("e: " + str(frase.count("e")))
print("i: " + str(frase.count("i")))
print("o: " + str(frase.count("o")))
print("u: " + str(frase.count("o")))