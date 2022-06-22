v = int(input('Digite o valor em Reais \n R$:'))
usd = float(v/3.27)
print('Com R${} você pode comprar US${:.2f}'.format(v, usd))
