"""
(Entrada de dados - Tipo do dado)
Escreva um programa em Python que receba dois números inteiros
(Processamento - calculo - dados que estão em memória)
e calcule a diferença entre os dois e em seguida apresente
(Processamento - cálculo)
o seu sucessor e antecessor.
(Exibição do resultado)
"""
valorA = 0
valorB = 0
diferenca = 0
sucessor = 0
antecessor = 0

valorA = int(input("Valor de A? "))
valorB = int(input("Valor de B? "))


diferenca = valorA - valorB

sucessor = diferenca + 1
antecessor = diferenca - 1
print("Valor A: %d , Valor B: %d " % (valorA, valorB))
print("Diferença entre os dois números %d ." % (diferenca))
print("O número sucessor é %d e o antecessor é %d " % (sucessor, antecessor))