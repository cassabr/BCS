# 19. 

# Construa um programa que solicite o tamanho em megabytes de um arquivo para transferência, 
# e a velocidade do link de internet em megabits por segundo. 

# Compute o tempo de transferência do arquivo, passando por esse link em minutos. 
# Imprima o resultado na tela. Dica: 1 MB são 1000000 de bytes e 1 byte são 8 bits.

arquivo = input("Tamanho do arquivo em MB: ")

link = input("Velocidade do link em Mbps: ")

tempo = (arquivo*8.0/link)/60.0

print("Tempo: " + str(tempo) + "minutos")