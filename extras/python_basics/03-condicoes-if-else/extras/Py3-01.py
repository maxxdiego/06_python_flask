# Condições simples

# Placeholder %s (string) / %d (number)

# saldo é R$ 100,00
# pode sacar qualquer valor até R$ 100,00
# sacar R$ 80,00 - ok saldo restante R$ 20,00
# sacar R$ 10,00 - ok saldo restante R$ 10,00
# sacar R$ 25,00 - negado sem saldo
# IF ELSE

saldo = 100

if saldo>=0: print(" Seu Saldo Atual é R$ %d " % (saldo))

if saldo<0: print(" Seu Saldo Atual é (negativo) R$ %d " % (saldo))

valorSaque = 80

if saldo-valorSaque>=0: print("Saque efetuado - R$ %d " % (valorSaque))

saldo = saldo - valorSaque

if saldo>=0: print(" Seu Saldo Atual é R$ %d " % (saldo))

valorSaque = 10

if saldo-valorSaque>=0: print("Saque efetuado - R$ %d " % (valorSaque))

saldo = saldo - valorSaque

if saldo>=0: print(" Seu Saldo Atual é R$ %d " % (saldo))

valorSaque = 25

if saldo-valorSaque<0: 
  print("Saque não efetuado no valor de R$ %d " % (valorSaque))

if saldo>=0: print(" Seu Saldo Atual é R$ %d " % (saldo))