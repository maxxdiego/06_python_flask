# Escrever um algoritmo que receba o valor com o preçi da gasolina e do ethanol.
# Calcule a diferença de valores entre ethanol e gaslina
# Se o resultado for inferior a 0,7, o alcool é o melhor para abastecer.
# Se o resultado for maior que o,7, então a gasolina é melhor.

precoEthanol = float(input("Digite o preço do Ethanol : "))
precoGasolina = float(input("Digite o preço do Ethanol : "))

diferenca = 0.00

if(precoGasolina > 0):
    diferenca = precoEthanol / precoGasolina
    print("A diferença entre Ethanol x Gasolina é :", diferenca)
    if(diferenca<0.7):
        print("Abasteça com Ethanol.")
    else:
        print("Abasteça com Gasolina.")
else:
    print("Informe todos os dados.")