larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
tinta = área /2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))