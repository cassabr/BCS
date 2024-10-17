# 8. 
# Agora, usando o dicionário do exercício anterior, imprima todos os itens do dicionário na forma chave: valor.

carro = {
    "Marca" : "Ford",
    "Modelo" : "Fiesta",
    "Placa" : "FBD4986",
    "Ano" : 2011
}

for item in carro.items():
    print(item[0], ":", item[1])
