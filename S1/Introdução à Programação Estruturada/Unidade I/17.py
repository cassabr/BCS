# 17. 
# Construa um aplicativo para uma loja de pisos. 
# O aplicativo solicita o tamanho em metros quadrados da área a ser colocado o piso. 
# Cada piso tem 60 × 60 centímetros; eles são vendidos em caixas com 10 pisos, que custam R$ 70,00. 
# Mostre na tela para o cliente a quantidade de caixas que ele deve comprar e o preço total do orçamento.

m2 = int(input("Digite o tamanho da área: "))

cxs = m2 / (0.6 * 0.6 * 10)

cxss = cxs + 1

a = cxs - int(cxs) 
print(a)
      
if (cxs - int(cxs) > 0.001):
    preco = int(cxss) * 70
    print("Para cobrir",m2, "m2 de área serão necessárias", int(cxss), "que no total ficará por R$",preco)
else:
    preco = int(cxs) * 70
    print("Para cobrir",m2, "m2 de área serão necessárias", int(cxs), "que no total saem por R$",preco)