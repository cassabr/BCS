# 17. 
# Construa um aplicativo para uma loja de pisos. 
# O aplicativo solicita o tamanho em metros quadrados da área a ser colocado o piso. 
# Cada piso tem 60 × 60 centímetros; eles são vendidos em caixas com 10 pisos, que custam R$ 70,00. 
# Mostre na tela para o cliente a quantidade de caixas que ele deve comprar e o preço total do orçamento.


metros = int(input("Digite o tamanho da área: "))

caixa = (0.6 * 0.6 * 10)

total = (metros//caixa)+1

print("Comprar caixas: " + str(total))

print("Valor: " + str(total*70.00))