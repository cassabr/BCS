# 14. Crie um programa que receba como a entrada a altura da pessoa e calcule o peso ideal. 
# Utilize as fórmulas: para os homens, (72.7*altura) – 58; para as mulheres, (62.1*altura) - 44.7

genero = str(input("Qual o seu gênero? (H/M) "))

altura = float(input("Qual a sua altura em metros? "))

if 1 < altura < 2.2:
    if genero == "H" or genero == "h":
        imc = (72.7*altura) - 58
        print("Seu IMC é: ", imc)
    if genero == "M" or genero == "m":
        imc = (62.1*altura) - 44.7
        print("Seu IMC é: ", imc)
    else:
        print("Não entendi.")
else:
    print("A altura digitada deve estar errada. Tente novamente.")