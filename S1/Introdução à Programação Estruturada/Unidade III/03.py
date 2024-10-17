# 3. 
# Faça um programa que descubra se uma palavra é ou não um palíndromo. 
# Um palíndromo é uma sequência de caracteres que, quando lidos do fim para o começo, são idênticos à palavra original.
# Exemplos: Ana, ovo, osso, ama e arara são palíndromos.

def palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
print(palindromo("ovo"))

print(palindromo("osso"))

print(palindromo("lasca"))

print(palindromo("ana"))

print(palindromo("lisa"))