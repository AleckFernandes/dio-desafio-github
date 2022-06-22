a = float(input('Digite Lagura x Altura da parede para o calculo \n Altura:'))
l = float(input('\n Largura:'))
m = a*l
m2 = m/2
print('Sua parede possui {:.2f}m2, para pinta-lá você irá precisar de {:.2f} litros de tinta'.format(m, m2))