# Utilizando o %s como placeholder para concatenar strings
primeironome = input("Digite seu nome: ")
telefone = input("Digite se número de telefone: ")
email = input("Digite seu melhor e-mail: ")
textoDigitado = "Nome: %s - Telefone: %s - e-mail: %s" % (primeironome, telefone, email)
print(textoDigitado)