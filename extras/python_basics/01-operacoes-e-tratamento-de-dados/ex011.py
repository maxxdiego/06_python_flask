preço = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Quantos % de desconto será aplicado? '))
novo = preço - (preço * desconto/100)
print('O produto que custava R${:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}'.format(preço, desconto, novo))