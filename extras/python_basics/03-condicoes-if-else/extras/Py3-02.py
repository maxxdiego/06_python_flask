# saldo é R$ 100,00
# pode sacar qualquer valor até R$ 100,00
# sacar R$ 80,00 - ok saldo restante R$ 20,00
# sacar R$ 10,00 - ok saldo restante R$ 10,00
# sacar R$ 25,00 - negado sem saldo
# IF ELSE IF

saldo = 100

if saldo>=0:
   print(" Seu Saldo Atual é R$ %d " % (saldo))
else:
   print(" Seu Saldo Atual é (negativo) R$ %d " % (saldo))

valorSaque = 80

if (saldo-valorSaque)>=0: 
  print("Saque efetuado - R$ %d " % (valorSaque))
  saldo = saldo - valorSaque
  print(" Seu Saldo Atual é R$ %d " % (saldo))
else:
  print(" Seu Saldo Atual é R$ %d " % (saldo))
  print(" Saque não efetuado no valor de R$ %d " % (valorSaque))


valorSaque = 10

if (saldo-valorSaque)>=0: 
  print("Saque efetuado - R$ %d " % (valorSaque))
  saldo = saldo - valorSaque
  print(" Seu Saldo Atual é R$ %d " % (saldo))
else:
  print(" Seu Saldo Atual é R$ %d " % (saldo))
  print(" Saque não efetuado no valor de R$ %d " % (valorSaque))


valorSaque = 25

if (saldo-valorSaque)>=0: 
  print("Saque efetuado - R$ %d " % (valorSaque))
  saldo = saldo - valorSaque
  print(" Seu Saldo Atual é R$ %d " % (saldo))
else:  
  print(" Saque não efetuado no valor de R$ %d " % (valorSaque))