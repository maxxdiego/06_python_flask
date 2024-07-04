from time import sleep
num = int(input('Digite um número para ver sua tabuada:'))
print('--'*12)
print('Gerando tabuada do {}...'.format(num))
print('--'*12)
sleep(3)
for c in range(1,11):
    print('{} x {:2} = {}'.format(num,c,num*c))
print('--'*12)