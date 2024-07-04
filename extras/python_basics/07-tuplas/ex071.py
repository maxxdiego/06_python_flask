cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num].upper()}.')
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()
        if continuar == 'N':
            print('Programa finalizado! Até breve!')
            break
    else:
        print('Tente novamente. ', end='')
