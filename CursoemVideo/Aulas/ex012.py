valor = float(input('Valor do Produto sem desconto:'))
desconto = float(input('Valor do Desconto:'))
desconto = desconto/100
desconto2 = desconto * valor
desconto3 = valor - desconto2
print('Valor Originalmente: R${} Novo Valor do Produto: R${}'.format(valor, desconto3))
