# 9. 
# Faça um programa que pergunte ao usuário o valor que ele tem investido e a taxa percentual que ele ganha ao mês 
# (juros simples). Calcule e imprima o total ganho com o investimento em 3 meses.

meses = 3

investido = int(input("Qual o seu valor investido? "))

taxa = int(input("Qual a taxa percentual mensal? "))

ganho = investido * meses * (taxa/100)

print("Retorno depois de ", meses,"será ", ganho)