from time import sleep
print('Contagem regressiva para o fim do ano:')
for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
print('Feliz Ano Novo!')