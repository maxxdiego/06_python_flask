# coleta de dados valor sempre positivo
# quantidade de vendas - contador
# valor médio das vendas
# valor total das vendas

# enquanto o número -1

# \n salto de linha

dadoVenda = 0
contador = 0
valorMedioDasVendas = 0
valorTotalDasVendas = 0

while dadoVenda>=0:
   dadoVenda = int(input("Digite o valor da venda, ou -1 para finalizar.\n"))
   if dadoVenda>=0:
    contador = contador + 1
    valorTotalDasVendas = valorTotalDasVendas + dadoVenda
valorMedioDasVendas = valorTotalDasVendas / contador
print("Total das Vendas: %d " % (valorTotalDasVendas))
print("Média das Vendas: %d " % (valorMedioDasVendas))
print("Quantida de vendas: %d " % (contador))