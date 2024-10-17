# 2. 
# Crie um programa com a função chamada ‘positivo’ que recebe um número 
# e retorne verdadeiro se ele for positivo e falso se ele é negativo. Imprima o resultado.

def positivo (n):
    if n >= 0:
        return True
    else:
        return False

print(positivo(3))

print(positivo(-1))
