from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = int(input('''Digite seu sexo:
[ 1 ] para masculino
[ 2 ] para feminino
[   ]: '''))
if sexo == 2:
    print('O seu alistamento não é obrigatório pois é do sexo feminino.')
elif sexo == 1:
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Opção inválida. Tente novamente.')