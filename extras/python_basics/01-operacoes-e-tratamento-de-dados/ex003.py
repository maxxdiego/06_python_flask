"""
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão
"""

# nome = input('Qual seu nome? ')
# print('Prazer, {:=^20}'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
# print('A soma vale {}'.format(n1+n2))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma é {}, subtração é {}, a multiplicação é {}, a divisão é {:.2f}, \nA divisão inteira é {} e a potência é {}.'.format(s,sub,m,d,di,p))

#end='' - deixa na mesma linha, em caso de dois ou mais prints
#\n - quebra linha.